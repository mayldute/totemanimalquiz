from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Answer:
    text: str
    points: dict[str, int]


@dataclass(frozen=True, slots=True)
class Question:
    text: str
    answers: tuple[Answer, ...]
    image_url: str


@dataclass(frozen=True, slots=True)
class AnimalResult:
    name: str
    description: str
    image_url: str
    details_url: str


@dataclass(slots=True)
class QuizState:
    current_question: int = 0
    scores: dict[str, int] = field(default_factory=dict)
    last_interaction: float = 0.0
