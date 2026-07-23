import logging
from io import BytesIO

import redis
import requests
from redis import Redis

logger = logging.getLogger(__name__)

IMAGE_CACHE_TTL_SECONDS = 3600
REQUEST_TIMEOUT_SECONDS = 10


class ImageCache:
    def __init__(self, redis_url: str) -> None:
        self._client = self._connect(redis_url)

    @staticmethod
    def _connect(redis_url: str) -> Redis | None:
        client = redis.from_url(redis_url)
        try:
            client.ping()
        except redis.RedisError:
            logger.warning("Redis is unavailable; images will not be cached.")
            return None
        return client

    def get_image(self, image_url: str) -> BytesIO | str:
        cached_image = self._read_cache(image_url)
        if cached_image is not None:
            return self._as_file(cached_image)

        image = self._download(image_url)
        if image is None:
            return image_url

        self._write_cache(image_url, image)
        return self._as_file(image)

    def _read_cache(self, image_url: str) -> bytes | None:
        if self._client is None:
            return None
        try:
            value = self._client.get(image_url)
        except redis.RedisError:
            logger.exception("Could not read image from Redis.")
            return None
        return value if isinstance(value, bytes) else None

    def _write_cache(self, image_url: str, image: bytes) -> None:
        if self._client is None:
            return
        try:
            self._client.setex(image_url, IMAGE_CACHE_TTL_SECONDS, image)
        except redis.RedisError:
            logger.exception("Could not cache image in Redis.")

    @staticmethod
    def _download(image_url: str) -> bytes | None:
        try:
            response = requests.get(image_url, timeout=REQUEST_TIMEOUT_SECONDS)
            response.raise_for_status()
        except requests.RequestException:
            logger.exception("Could not download image: %s", image_url)
            return None
        return response.content

    @staticmethod
    def _as_file(image: bytes) -> BytesIO:
        file = BytesIO(image)
        file.name = "image.jpg"
        return file
