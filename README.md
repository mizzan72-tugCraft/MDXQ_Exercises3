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
│   ├── 20250909_Exercises3_Challenge_rf100_0909-1257.ipynb
│   ├── 20250909_Exercises3_Challenge_rf200_0909-1318.ipynb
│   ├── 20250909_Exercises3_Challenge_TEMPLATE.ipynb
│   ├── score_analysis.py          # スコア記録・分析ライブラリ
│   └── theme1_sample_code.ipynb
├── submissions/                   # 提出ファイル
│   └── 20250909_Exercises3_Challenge_rf100_0909-1229.csv
├── .gitignore
└── README.md
```

## ファイル命名規則

### **基本形式**
```
[YYYYMMDD]_Exercises3_Challenge_[改善内容]_[MMdd-HHmm].ipynb
[YYYYMMDD]_Exercises3_Challenge_[改善内容]_[MMdd-HHmm].csv
```

### **具体例**
```
# Notebook
20250909_Exercises3_Challenge_rf100_0909-1257.ipynb
20250909_Exercises3_Challenge_rf200_0909-1318.ipynb
20250909_Exercises3_Challenge_xgb_0909-1330.ipynb

# 提出ファイル
20250909_Exercises3_Challenge_rf100_0909-1229.csv
20250909_Exercises3_Challenge_rf200_0909-1319.csv
20250909_Exercises3_Challenge_xgb_0909-1331.csv
```

### **命名規則の説明**
- **YYYYMMDD**: 作成日（2025年9月9日）
- **Exercises3**: 課題名
- **Challenge**: チャレンジ名
- **[改善内容]**: 実施した改善（rf100, rf200, xgb, features等）
- **[MMdd-HHmm]**: 作成時刻（月日-時分）

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

### 2. 新しい改善を試す際の手順

```bash
# 1. テンプレートから新しいNotebookを作成
cp 20250909_Exercises3_Challenge_TEMPLATE.ipynb 20250909_Exercises3_Challenge_[改善内容]_[MMdd-HHmm].ipynb

# 例:
cp 20250909_Exercises3_Challenge_TEMPLATE.ipynb 20250909_Exercises3_Challenge_rf200_0909-1330.ipynb
cp 20250909_Exercises3_Challenge_TEMPLATE.ipynb 20250909_Exercises3_Challenge_xgb_0909-1345.ipynb
cp 20250909_Exercises3_Challenge_TEMPLATE.ipynb 20250909_Exercises3_Challenge_features_0909-1400.ipynb

# 2. Notebookを編集
# - improvement_name を適切な値に変更
# - モデルや特徴量を調整

# 3. 実行して提出ファイルを生成

# 4. 結果をコミット
git add notebooks/20250909_Exercises3_Challenge_[改善内容]_[MMdd-HHmm].ipynb
git add submissions/20250909_Exercises3_Challenge_[改善内容]_[MMdd-HHmm].csv
git commit -m "改善: [改善内容] - スコア: [スコア値]"
```

### 3. スコア記録・分析

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

| ファイル名 | モデル | スコア | 改善率 | 施策 |
|------------|--------|--------|--------|------|
| 20250909_Exercises3_Challenge_rf100_0909-1257.ipynb | RandomForestRegressor (100) | 3.072567 | 23.07% | 線形回帰からRandomForestに変更 |

## 今後の改善案

- [ ] ハイパーパラメータの調整（n_estimators, max_depth等）
- [ ] 特徴量エンジニアリング（ラグ特徴量、統計特徴量等）
- [ ] 他のモデルの試行（XGBoost, LightGBM等）
- [ ] データの前処理改善（外れ値処理、スケーリング等）

## ライセンス

このプロジェクトは学習目的で作成されています。
