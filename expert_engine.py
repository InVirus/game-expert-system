from typing import List, Dict, Any, Optional
from knowledge_base import GAMES, KNOWLEDGE_BASE, GAME_METADATA
def calculate_results(selected_answers: List[str]) -> List[Dict[str, Any]]:
    scores: Dict[str, int] = {game: 0 for game in GAMES}
    for answer_id in selected_answers:
        weights = KNOWLEDGE_BASE.get(answer_id, {})
        for game, weight in weights.items():
            scores[game] += weight
    max_possible_score = len(selected_answers) * 5 if selected_answers else 1
    ranking: List[Dict[str, Any]] = []
    for game, score in scores.items():
        percentage = round((score / max_possible_score) * 100)
        metadata = GAME_METADATA.get(game, {})
        ranking.append({
            "game": game,
            "score": score,
            "max_score": max_possible_score,
            "percentage": percentage,
            "genre": metadata.get("genre", ""),
            "developer": metadata.get("developer", ""),
            "description": metadata.get("description", ""),
            "tag": metadata.get("tag", "")
        })
    ranking.sort(key=lambda item: item["score"], reverse=True)
    return ranking
def get_explanation(
    selected_answers: List[str],
    selected_labels: List[str],
    selected_categories: List[str],
    game: str
) -> List[Dict[str, Any]]:
    explanation: List[Dict[str, Any]] = []
    for answer_id, answer_text, category in zip(
        selected_answers, selected_labels, selected_categories
    ):
        weight = KNOWLEDGE_BASE.get(answer_id, {}).get(game, 0)
        explanation.append({
            "category": category,
            "criterion": answer_text,
            "weight": weight,
            "max_weight": 5
        })
    return explanation
def get_alternative(ranking: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    if len(ranking) > 1:
        return ranking[1]
    return None
