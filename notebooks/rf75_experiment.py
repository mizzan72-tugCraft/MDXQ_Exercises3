# =============================================================================
# RandomForest n_estimators=75 単体実験
# =============================================================================
# 
# 【実験目的】
# - n_estimators=75が最適値という仮説の検証
# - 現在のベスト（n_estimators=100, スコア3.07256739424164）との比較
# - 計算効率と予測精度のバランス確認
# 
# 【期待される結果】
# - スコア: 3.065-3.075 (現在のベストと同等以上)
# - 学習時間: 約25%短縮
# - 予測安定性: 十分な品質を維持
# 
# =============================================================================

import pandas as pd
import numpy as np
import datetime
import time
from sklearn.ensemble import RandomForestRegressor
import os

def main():
    print("=" * 70)
    print("🎯 RandomForest n_estimators=75 最適化実験")
    print("=" * 70)
    print("仮説: n_estimators=75が計算効率と予測精度の最適バランス")
    print("=" * 70)
    
    # データ読み込み
    print("\n📁 データ読み込み中...")
    base_dir = '../data/'
    
    try:
        sales_df = pd.read_csv(base_dir + 'sales_history.csv')
        item_categories_df = pd.read_csv(base_dir + 'item_categories.csv')
        category_names_df = pd.read_csv(base_dir + 'category_names.csv')
        test_df = pd.read_csv(base_dir + 'test.csv')
        submission_df = pd.read_csv(base_dir + 'sample_submission.csv', header=None)
        print("✅ データ読み込み完了")
    except FileNotFoundError as e:
        print(f"❌ データファイルが見つかりません: {e}")
        return
    
    # データ前処理（ベストモデルと同一の処理）
    print("\n🔧 データ前処理中...")
    
    # 日付から年と月を抽出
    sales_df['年'] = sales_df['日付'].apply(lambda x: x.split('-')[0])
    sales_df['月'] = sales_df['日付'].apply(lambda x: x.split('-')[1])
    
    # 月ごとの売上個数を集計
    sales_month_df = sales_df.groupby(['商品ID', '店舗ID', '年', '月'])['売上個数'].sum().reset_index()
    
    # 商品カテゴリIDを結合
    train_df = pd.merge(sales_month_df, item_categories_df, on='商品ID', how='left')
    
    # データ型を変換
    train_df['年'] = train_df['年'].astype(int)
    train_df['月'] = train_df['月'].astype(int)
    
    # test_dfにも年と月を追加し、商品カテゴリIDを結合
    test_df['年'] = 2022
    test_df['月'] = 12
    test_df = pd.merge(test_df, item_categories_df, on='商品ID', how='left')
    
    # 特徴量とターゲット変数を定義
    feature_columns = ['店舗ID', '商品ID', '年', '月', '商品カテゴリID']
    target_column = '売上個数'
    
    # 学習データとテストデータに分割
    X_train = train_df[feature_columns]
    y_train = train_df[target_column]
    X_test = test_df[feature_columns]
    
    print(f"✅ データ前処理完了")
    print(f"   訓練データ形状: {X_train.shape}")
    print(f"   テストデータ形状: {X_test.shape}")
    print(f"   使用特徴量: {', '.join(feature_columns)}")
    
    # モデル学習（n_estimators=75）
    print(f"\n🌳 RandomForest学習中 (n_estimators=75)...")
    
    start_time = time.time()
    
    # モデル定義（ベストモデルと同じ設定、n_estimatorsのみ変更）
    model = RandomForestRegressor(
        n_estimators=75,
        random_state=42,
        n_jobs=-1  # 全CPUコアを使用
    )
    
    # 学習実行
    model.fit(X_train, y_train)
    
    training_time = time.time() - start_time
    
    print(f"✅ 学習完了")
    print(f"   学習時間: {training_time:.2f}秒")
    
    # 予測実行
    print(f"\n🔮 予測実行中...")
    
    predict_start = time.time()
    y_pred = model.predict(X_test)
    predict_time = time.time() - predict_start
    
    # 負の値を0に変換
    y_pred[y_pred < 0] = 0
    
    print(f"✅ 予測完了")
    print(f"   予測時間: {predict_time:.3f}秒")
    print(f"   予測結果の形状: {y_pred.shape}")
    print(f"   予測値の範囲: {y_pred.min():.2f} ～ {y_pred.max():.2f}")
    print(f"   予測値の平均: {y_pred.mean():.2f}")
    print(f"   予測値の標準偏差: {y_pred.std():.2f}")
    
    # 特徴量重要度の表示
    print(f"\n📊 特徴量重要度:")
    feature_importance = model.feature_importances_
    for feature, importance in zip(feature_columns, feature_importance):
        print(f"   {feature}: {importance:.4f}")
    
    # 提出ファイル生成
    print(f"\n📄 提出ファイル生成中...")
    
    # 現在の日時でタイムスタンプ生成
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    
    # 提出用データフレーム作成
    submission_copy = submission_df.copy()
    submission_copy[1] = y_pred
    
    # ファイル名生成
    submission_filename = f'../submissions/{timestamp}_Exercises3_Challenge_rf75_optimal.csv'
    
    # ディレクトリが存在しない場合は作成
    os.makedirs('../submissions', exist_ok=True)
    
    # CSVファイル出力
    submission_copy.to_csv(submission_filename, index=False, header=False)
    
    print(f"✅ 提出ファイル生成完了")
    print(f"   ファイル名: {submission_filename}")
    
    # 結果サマリー
    print(f"\n" + "=" * 70)
    print(f"📋 実験結果サマリー")
    print(f"=" * 70)
    print(f"モデル設定:")
    print(f"  - アルゴリズム: RandomForestRegressor")
    print(f"  - n_estimators: 75")
    print(f"  - random_state: 42")
    print(f"  - 使用特徴量: {len(feature_columns)}個")
    print(f"")
    print(f"パフォーマンス:")
    print(f"  - 学習時間: {training_time:.2f}秒")
    print(f"  - 予測時間: {predict_time:.3f}秒")
    print(f"  - 予測値範囲: {y_pred.min():.2f} ～ {y_pred.max():.2f}")
    print(f"  - 予測値平均: {y_pred.mean():.2f}")
    print(f"")
    print(f"期待される結果:")
    print(f"  - 現在のベストスコア: 3.07256739424164 (n_estimators=100)")
    print(f"  - 期待スコア範囲: 3.065 ～ 3.075")
    print(f"  - 期待される改善: 計算時間25%短縮 + 同等以上の性能")
    print(f"")
    print(f"次のステップ:")
    print(f"  1. 提出ファイルをコンペティションサイトにアップロード")
    print(f"  2. スコア結果を記録・分析")
    print(f"  3. 結果に基づいて更なる最適化を検討")
    print(f"=" * 70)
    
    # スコア記録用コード生成
    print(f"\n📝 スコア記録用コード（提出後に実行）:")
    print(f"=" * 50)
    print(f"from score_analysis import record_score")
    print(f"")
    print(f"# 提出後にスコアを入力してください")
    print(f"score_rf75 = None  # 例: 3.070000")
    print(f"")
    print(f"if score_rf75 is not None:")
    print(f"    result = record_score(")
    print(f"        current_score=score_rf75,")
    print(f"        model_name='RandomForestRegressor (n_estimators=75)',")
    print(f"        features_used='店舗ID, 商品ID, 年, 月, 商品カテゴリID',")
    print(f"        notes='最適化実験: n_estimators=75'")
    print(f"    )")
    print(f"    print('スコア記録完了!')")
    print(f"else:")
    print(f"    print('スコアを入力してからコードを実行してください')")
    print(f"=" * 50)

if __name__ == "__main__":
    main()