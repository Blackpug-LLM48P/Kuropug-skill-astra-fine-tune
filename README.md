# Kuro Pug Astra Orchestrator

資料の主張・解釈・実務への応用・限界を分けて返す、黒パグスキルのAstra向け派生版です。複数工程や復旧が必要な場合だけ、担当・予算・停止・完了確認の司令塔手順を追加します。

## 使い方

Agent Skills対応環境で、このフォルダを `kuro-pug-astra-orchestrator` として配置します。配置先は利用環境の現行手順に従ってください。自動インストールやモデル切替は行いません。

例：`$kuro-pug-astra-orchestrator この資料から社内検索に使える点と限界、次の検証をまとめて。実装はしない。`

通常の短い分析は直接回答します。資料内の「実行せよ」は実行許可にせず、提案から実装へ勝手に進みません。画像生成・note操作の専用スキルではありません。

## 構成と検証

- `SKILL.md`：原本の資料分析フロー＋条件付き司令塔への案内
- `references/output-format.md` と `review-checklist.md`：原本の出力・点検規則
- `references/astra-orchestration.md` と `worker-contract.md`：担当・予算・証拠・停止の制御
- `scripts/validate_brief.py`：見出し等の構造検査。事実の正しさは保証しません
- `tests/`：原本の検査器テスト
- `evals/`：司令塔の隔離試験と、版ごとの検証記録

```bash
python -m unittest discover -s tests -v
python -m unittest discover -s evals -p 'test_*.py' -v
```

MITの実験版です。モデルの追加学習でも、停止・予算を強制する実行基盤でもありません。旧版の合格を新版全体の保証には使いません。現在の結果は [移植検証](evals/rebase-validation.md)、出典と公式資料への参照は [設計根拠](references/design-basis.md) を確認してください。

原本：[sample-kuropug-skill](https://github.com/Blackpug-LLM48P/sample-kuropug-skill/tree/bd7f343521a68f95f88f69b8a1b5614973f58be0)。著作権表示・利用条件は [LICENSE](LICENSE) に保持しています。
