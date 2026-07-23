# Totem Animal Quiz Bot

A Telegram quiz bot that asks users seven personality questions and matches them with an animal from the Moscow Zoo.

## Features

- Interactive seven-question quiz
- Typed quiz data built with Python dataclasses
- Personalized animal result with an image and information link
- Redis image cache with graceful fallback when Redis is unavailable
- Support and feedback forwarding to the administrator
- Social sharing buttons
- Automatic cleanup of inactive in-memory quiz sessions
- Unit tests for quiz logic and state storage

## Technology stack

- Python 3.12+
- PyTelegramBotAPI
- Redis
- Requests
- python-dotenv
- uv
- pytest
- Ruff

## Project structure

```text
totem-animal-quiz-bot/
├── src/totem_animal_bot/
│   ├── cache.py
│   ├── config.py
│   ├── data.py
│   ├── handlers.py
│   ├── keyboards.py
│   ├── main.py
│   ├── models.py
│   ├── quiz.py
│   └── state.py
├── tests/
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

## Installation

Install [uv](https://docs.astral.sh/uv/) and clone the repository.

```bash
git clone https://github.com/mayldute/totemanimalquiz
cd totem-animal-quiz-bot
uv sync --extra dev
```

## Environment variables

Copy the example file:

```bash
cp .env.example .env
```

Fill in the values:

```env
TOKEN=your_telegram_bot_token
ADMIN_ID=123456789
BOT_USERNAME=YourBotUsername
REDIS_URL=redis://localhost:6379/0
```

Do not add `.env` to Git.

## Redis

Run Redis locally with Docker:

```bash
docker run --name totem-animal-redis -p 6379:6379 -d redis:7-alpine
```

The bot can still run when Redis is unavailable, but images will not be cached.

## Run the bot

```bash
uv run totem-animal-bot
```

## Tests and code quality

```bash
uv run pytest
uv run ruff format .
uv run ruff check .
```
