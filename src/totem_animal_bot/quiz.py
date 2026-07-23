from collections.abc import Mapping


class EmptyScoreError(ValueError):
    """Raised when a result is requested before any score was recorded."""


def add_points(scores: dict[str, int], answer_points: Mapping[str, int]) -> None:
    for animal, points in answer_points.items():
        scores[animal] = scores.get(animal, 0) + points


def determine_result(scores: Mapping[str, int]) -> str:
    if not scores:
        raise EmptyScoreError("Cannot determine a result from empty scores.")

    return max(scores, key=scores.get)
