import threading
import time

from .models import QuizState


class UserStateStorage:
    def __init__(self) -> None:
        self._states: dict[int, QuizState] = {}
        self._lock = threading.RLock()

    def create(self, user_id: int) -> QuizState:
        state = QuizState(last_interaction=time.time())
        with self._lock:
            self._states[user_id] = state
        return state

    def get(self, user_id: int) -> QuizState | None:
        with self._lock:
            return self._states.get(user_id)

    def get_or_create(self, user_id: int) -> QuizState:
        with self._lock:
            state = self._states.get(user_id)
            if state is None:
                state = QuizState(last_interaction=time.time())
                self._states[user_id] = state
            return state

    def reset(self, user_id: int) -> QuizState:
        return self.create(user_id)

    def touch(self, user_id: int) -> None:
        with self._lock:
            state = self._states.get(user_id)
            if state is not None:
                state.last_interaction = time.time()

    def remove_inactive(
        self,
        *,
        lifetime_seconds: int,
        current_time: float | None = None,
    ) -> int:
        now = current_time if current_time is not None else time.time()

        with self._lock:
            inactive_ids = [
                user_id
                for user_id, state in self._states.items()
                if now - state.last_interaction > lifetime_seconds
            ]
            for user_id in inactive_ids:
                del self._states[user_id]

        return len(inactive_ids)
