import logging
import threading
import time

from telebot import TeleBot

from .cache import ImageCache
from .config import load_settings
from .handlers import register_handlers
from .state import UserStateStorage

USER_DATA_LIFETIME_SECONDS = 24 * 60 * 60
CLEANUP_INTERVAL_SECONDS = 60 * 60


def cleanup_inactive_users(storage: UserStateStorage) -> None:
    logger = logging.getLogger(__name__)
    while True:
        removed_count = storage.remove_inactive(
            lifetime_seconds=USER_DATA_LIFETIME_SECONDS
        )
        logger.info("Removed %s inactive user sessions.", removed_count)
        time.sleep(CLEANUP_INTERVAL_SECONDS)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    settings = load_settings()
    storage = UserStateStorage()
    image_cache = ImageCache(settings.redis_url)
    bot = TeleBot(settings.token)

    register_handlers(
        bot,
        settings=settings,
        storage=storage,
        image_cache=image_cache,
    )

    cleanup_thread = threading.Thread(
        target=cleanup_inactive_users,
        args=(storage,),
        daemon=True,
        name="user-state-cleanup",
    )
    cleanup_thread.start()

    logging.getLogger(__name__).info("Bot started.")
    bot.infinity_polling(
        skip_pending=True,
        timeout=20,
        long_polling_timeout=20,
    )


if __name__ == "__main__":
    main()
