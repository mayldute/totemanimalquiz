from totem_animal_bot.state import UserStateStorage


def test_get_or_create_creates_state() -> None:
    storage = UserStateStorage()
    state = storage.get_or_create(123)
    assert state.current_question == 0
    assert state.scores == {}


def test_reset_replaces_existing_state() -> None:
    storage = UserStateStorage()
    state = storage.create(123)
    state.current_question = 4
    state.scores["Snow Leopard"] = 10

    reset_state = storage.reset(123)

    assert reset_state.current_question == 0
    assert reset_state.scores == {}


def test_remove_inactive_users() -> None:
    storage = UserStateStorage()
    state = storage.create(123)
    state.last_interaction = 100.0

    removed_count = storage.remove_inactive(
        lifetime_seconds=50,
        current_time=200.0,
    )

    assert removed_count == 1
    assert storage.get(123) is None
