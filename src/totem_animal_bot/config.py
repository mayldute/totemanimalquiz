import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True, slots=True)
class Settings:
    token: str
    admin_id: int
    bot_username: str
    redis_url: str


def load_settings() -> Settings:
    load_dotenv()

    token = os.getenv("TOKEN")
    admin_id = os.getenv("ADMIN_ID")
    bot_username = os.getenv("BOT_USERNAME")
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

    if not token:
        raise RuntimeError("TOKEN environment variable is not configured.")
    if not admin_id:
        raise RuntimeError("ADMIN_ID environment variable is not configured.")
    if not bot_username:
        raise RuntimeError("BOT_USERNAME environment variable is not configured.")

    try:
        parsed_admin_id = int(admin_id)
    except ValueError as error:
        raise RuntimeError("ADMIN_ID must be an integer.") from error

    return Settings(
        token=token,
        admin_id=parsed_admin_id,
        bot_username=bot_username.removeprefix("@"),
        redis_url=redis_url,
    )
