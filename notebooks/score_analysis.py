# =============================================================================
# スコア記録・分析ライブラリ
# =============================================================================
# このファイルは、機械学習コンペティションのスコア記録・分析用の関数を提供します
# 
# 使用方法:
# from score_analysis import record_score, compare_scores, generate_improvement_summary
# 
# =============================================================================

import json
import os
import datetime

SCORE_HISTORY_FILE = "score_history.json"
BASELINE_SCORE = 3.9937572546850784

def _load_score_history():
    """スコア履歴を読み込む"""
    if os.path.exists(SCORE_HISTORY_FILE):
        with open(SCORE_HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def _save_score_history(history):
    """スコア履歴を保存する"""
    with open(SCORE_HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

def _get_previous_score():
    """直近のスコアを取得する"""
    history = _load_score_history()
    if history:
        return history[-1]['current_score']
    return BASELINE_SCORE

def record_score(current_score, model_name="", features_used="", notes=""):
    """
    スコアを記録し、改善状況を分析する関数（直近のスコアと比較）
    
    Parameters:
    -----------
    current_score : float
        現在のスコア
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
    
    # 直近のスコアを取得
    previous_score = _get_previous_score()
    
    # 直近のスコアとの比較
    improvement = previous_score - current_score
    improvement_rate = (improvement / previous_score) * 100
    
    # ベースラインとの比較
    baseline_improvement = BASELINE_SCORE - current_score
    baseline_improvement_rate = (baseline_improvement / BASELINE_SCORE) * 100
    
    # 履歴に追加
    history = _load_score_history()
    entry = {
        "timestamp": datetime.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "current_score": current_score,
        "model_name": model_name,
        "features_used": features_used,
        "notes": notes,
        "previous_score": previous_score,
        "improvement": improvement,
        "improvement_rate": improvement_rate,
        "baseline_improvement": baseline_improvement,
        "baseline_improvement_rate": baseline_improvement_rate
    }
    history.append(entry)
    _save_score_history(history)
    
    # 結果を表示
    print("=" * 60)
    print("📊 スコア分析結果")
    print("=" * 60)
    print(f"前回のスコア: {previous_score:.6f}")
    print(f"今回のスコア: {current_score:.6f}")
    print(f"改善幅: {improvement:.6f}")
    print(f"改善率: {improvement_rate:.2f}%")
    print(f"ベースラインからの改善率: {baseline_improvement_rate:.2f}%")
    
    if model_name:
        print(f"使用モデル: {model_name}")
    if features_used:
        print(f"使用特徴量: {features_used}")
    if notes:
        print(f"メモ: {notes}")
    
    print("-" * 60)
    if improvement > 0:
        print("✅ スコアが改善されました！")
        if improvement_rate > 5:
            print("🎉 大幅な改善です！")
        elif improvement_rate > 2:
            print("👍 良い改善です！")
        else:
            print("📈 少し改善されました")
    elif improvement == 0:
        print("➖ スコアに変化はありませんでした")
    else:
        print("❌ スコアが悪化しました。改善が必要です。")
    print("=" * 60)
    
    return entry

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

def generate_improvement_summary():
    """
    改善履歴のサマリーを生成する関数（履歴ファイルから読み込み）
    """
    
    history = _load_score_history()
    
    if not history:
        print("まだスコア記録がありません。")
        return
    
    print("=" * 60)
    print("📋 改善履歴サマリー")
    print("=" * 60)
    
    for i, entry in enumerate(history, 1):
        print(f"{i}. {entry['model_name'] or 'モデル未指定'}")
        print(f"   スコア: {entry['current_score']:.6f}")
        print(f"   前回からの改善率: {entry['improvement_rate']:.2f}%")
        print(f"   ベースラインからの改善率: {entry['baseline_improvement_rate']:.2f}%")
        if entry['notes']:
            print(f"   メモ: {entry['notes']}")
        print(f"   記録日時: {entry['timestamp']}")
        print()
    
    # 最良スコアを表示
    best_entry = min(history, key=lambda x: x['current_score'])
    print(f"🏆 最良スコア: {best_entry['current_score']:.6f} ({best_entry['model_name']})")
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
    
    # 使用例2: 改善履歴の表示
    generate_improvement_summary()
