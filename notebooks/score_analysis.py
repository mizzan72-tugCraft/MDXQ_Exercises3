# =============================================================================
# スコア記録・分析ライブラリ
# =============================================================================
# このファイルは、機械学習コンペティションのスコア記録・分析用の関数を提供します
# 
# 使用方法:
# from score_analysis import record_score, analyze_improvement
# 
# =============================================================================

def record_score(current_score, baseline_score=3.9937572546850784, 
                model_name="", features_used="", notes=""):
    """
    スコアを記録し、改善状況を分析する関数
    
    Parameters:
    -----------
    current_score : float
        現在のスコア
    baseline_score : float, default=3.9937572546850784
        ベースラインスコア（線形回帰）
    model_name : str, default=""
        使用したモデル名
    features_used : str, default=""
        使用した特徴量
    notes : str, default=""
        その他のメモ
    
    Returns:
    --------
    dict : 分析結果の辞書
    """
    
    improvement = baseline_score - current_score
    improvement_rate = (improvement / baseline_score) * 100
    
    result = {
        'baseline_score': baseline_score,
        'current_score': current_score,
        'improvement': improvement,
        'improvement_rate': improvement_rate,
        'model_name': model_name,
        'features_used': features_used,
        'notes': notes,
        'is_improved': improvement > 0
    }
    
    # 結果を表示
    print("=" * 60)
    print("📊 スコア分析結果")
    print("=" * 60)
    print(f"ベースラインスコア: {baseline_score:.6f}")
    print(f"今回のスコア: {current_score:.6f}")
    print(f"改善幅: {improvement:.6f}")
    print(f"改善率: {improvement_rate:.2f}%")
    
    if model_name:
        print(f"使用モデル: {model_name}")
    if features_used:
        print(f"使用特徴量: {features_used}")
    if notes:
        print(f"メモ: {notes}")
    
    print("-" * 60)
    if improvement > 0:
        print("✅ スコアが改善されました！")
        if improvement_rate > 10:
            print("🎉 大幅な改善です！")
        elif improvement_rate > 5:
            print("👍 良い改善です！")
        else:
            print("📈 少し改善されました")
    else:
        print("❌ スコアが悪化しました。改善が必要です。")
    print("=" * 60)
    
    return result

def compare_scores(scores_dict):
    """
    複数のスコアを比較する関数
    
    Parameters:
    -----------
    scores_dict : dict
        スコア名をキー、スコア値を値とする辞書
        例: {'baseline': 3.99, 'rf_100': 3.50, 'rf_200': 3.45}
    """
    
    print("=" * 60)
    print("📈 スコア比較")
    print("=" * 60)
    
    # スコアでソート
    sorted_scores = sorted(scores_dict.items(), key=lambda x: x[1])
    
    for i, (name, score) in enumerate(sorted_scores):
        rank = i + 1
        if rank == 1:
            print(f"🥇 {rank}位: {name} - {score:.6f} (最良)")
        elif rank == 2:
            print(f"🥈 {rank}位: {name} - {score:.6f}")
        elif rank == 3:
            print(f"🥉 {rank}位: {name} - {score:.6f}")
        else:
            print(f"   {rank}位: {name} - {score:.6f}")
    
    print("=" * 60)

def generate_improvement_summary(results_list):
    """
    改善履歴のサマリーを生成する関数
    
    Parameters:
    -----------
    results_list : list
        record_score()の結果のリスト
    """
    
    print("=" * 60)
    print("📋 改善履歴サマリー")
    print("=" * 60)
    
    for i, result in enumerate(results_list, 1):
        print(f"{i}. {result['model_name'] or 'モデル未指定'}")
        print(f"   スコア: {result['current_score']:.6f}")
        print(f"   改善率: {result['improvement_rate']:.2f}%")
        if result['notes']:
            print(f"   メモ: {result['notes']}")
        print()
    
    # 最良スコアを表示
    best_result = min(results_list, key=lambda x: x['current_score'])
    print(f"🏆 最良スコア: {best_result['current_score']:.6f} ({best_result['model_name']})")
    print("=" * 60)

# 使用例
if __name__ == "__main__":
    # 使用例1: 単一スコアの記録
    result1 = record_score(
        current_score=3.500000,
        model_name="RandomForestRegressor (n_estimators=100)",
        features_used="店舗ID, 商品ID, 年, 月, 商品カテゴリID",
        notes="線形回帰からRandomForestに変更"
    )
    
    # 使用例2: 複数スコアの比較
    scores = {
        'baseline': 3.9937572546850784,
        'rf_100': 3.500000,
        'rf_200': 3.450000
    }
    compare_scores(scores)
