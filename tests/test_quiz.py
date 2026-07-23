import pytest

from totem_animal_bot.quiz import EmptyScoreError, add_points, determine_result


def test_add_points_to_empty_scores() -> None:
    scores: dict[str, int] = {}
    add_points(scores, {"Snow Leopard": 3, "Amur Tiger": 2})
    assert scores == {"Snow Leopard": 3, "Amur Tiger": 2}


def test_add_points_accumulates_existing_score() -> None:
    scores = {"Snow Leopard": 2}
    add_points(scores, {"Snow Leopard": 3})
    assert scores["Snow Leopard"] == 5


def test_determine_result_returns_highest_score() -> None:
    assert determine_result({"Snow Leopard": 5, "Amur Tiger": 3}) == (
        "Snow Leopard"
    )


def test_determine_result_rejects_empty_scores() -> None:
    with pytest.raises(EmptyScoreError):
        determine_result({})
