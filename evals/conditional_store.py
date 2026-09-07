"""Isolated test fixture, NOT a production controller or skill enforcement layer.

Usage: python conditional_store.py DB init|read|write [expected_revision] [body]
init creates an absent SQLite database. First write simulates an external edit
immediately before compare-and-swap. Subsequent writes use normal revision checks.
Every read/write spends one fixture unit; 5 total, 1 reserved for final read.
"""
import json
import sqlite3
import sys
from pathlib import Path


def run(path, action, expected=None, body=None):
    if action == 'init':
        if Path(path).exists():
            raise ValueError('Refusing to overwrite existing fixture')
        with sqlite3.connect(path) as db:
            db.execute('CREATE TABLE artifact (revision INTEGER, body TEXT, spent INTEGER, injected INTEGER)')
            db.execute('INSERT INTO artifact VALUES (1, ?, 0, 0)', ('Title\nTypoo\n',))
        return {'initialized': True}
    if not Path(path).is_file():
        raise ValueError('Initialize a disposable fixture first')
    with sqlite3.connect(path) as db:
        db.execute('BEGIN IMMEDIATE')
        rev, old, spent, injected = db.execute('SELECT * FROM artifact').fetchone()
        if action not in ('read', 'write'):
            raise ValueError('Unknown action')
        if spent >= 5 or (action == 'write' and spent >= 4):
            return {'blocked': 'budget', 'spent': spent}
        spent += 1
        db.execute('UPDATE artifact SET spent=?', (spent,))
        if action == 'write':
            if not injected:
                rev += 1
                old += 'External footer\n'
                db.execute('UPDATE artifact SET revision=?, body=?, injected=1', (rev, old))
            if int(expected) != rev:
                return {'conflict': True, 'revision': rev, 'spent': spent}
            db.execute('UPDATE artifact SET revision=?, body=?', (rev + 1, body))
            return {'acknowledged': True, 'revision': rev + 1, 'spent': spent}
        return {'revision': rev, 'body': old, 'spent': spent}


if __name__ == '__main__':
    print(json.dumps(run(*sys.argv[1:]), ensure_ascii=False))
