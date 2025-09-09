# MDXQ Exercises3 - 小売業需要予測

## プロジェクト概要

このプロジェクトは、小売業の需要予測モデルを構築し、スコア改善を目指す機械学習コンペティション用のリポジトリです。

## 目標

- **ベースラインスコア**: 3.9937572546850784（線形回帰）
- **目標スコア**: 3.0以下

## ファイル構成

```
MDXQ/
├── data/                          # 元のデータファイル
│   ├── category_names.csv
│   ├── item_categories.csv
│   ├── sales_history.csv
│   ├── sample_submission.csv
│   ├── test.csv
│   └── データ説明.txt
├── notebooks/                     # Jupyter Notebook
│   ├── 20250909_enshu3_Challenge.ipynb
│   ├── score_analysis.py          # スコア記録・分析ライブラリ
│   └── theme1_sample_code.ipynb
├── submissions/                   # 提出ファイル
│   └── my_submission_rf_20250909-122900.csv
├── .gitignore
└── README.md
```

## 使用方法

### 1. 環境セットアップ

```bash
# リポジトリをクローン
git clone git@github.com:mizzan72-tugCraft/MDXQ_Exercises3.git
cd MDXQ_Exercises3

# Jupyter Notebookを起動
cd notebooks
jupyter notebook
```

### 2. スコア記録・分析

```python
from score_analysis import record_score, compare_scores

# スコア記録
result = record_score(
    current_score=3.500000,
    model_name="RandomForestRegressor",
    features_used="店舗ID, 商品ID, 年, 月, 商品カテゴリID",
    notes="線形回帰からRandomForestに変更"
)
```

## 改善履歴

| モデル | スコア | 改善率 | 施策 |
|--------|--------|--------|------|
| 線形回帰（ベースライン） | 3.9937572546850784 | - | - |
| RandomForestRegressor | [提出後記録] | [計算中] | 線形回帰からRandomForestに変更 |

## 今後の改善案

- [ ] ハイパーパラメータの調整（n_estimators, max_depth等）
- [ ] 特徴量エンジニアリング（ラグ特徴量、統計特徴量等）
- [ ] 他のモデルの試行（XGBoost, LightGBM等）
- [ ] データの前処理改善（外れ値処理、スケーリング等）

## ライセンス

このプロジェクトは学習目的で作成されています。
