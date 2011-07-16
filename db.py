import redis
import settings

class Db(object):
    """Db Singleton"""
    _redis_cli = None
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Db, cls).__new__(
                                cls)
        return cls._instance

    @property
    def client(self):
        if not self._redis_cli:
            self._redis_cli = redis.Redis(settings.REDIS_HOST)
        return self._redis_cli

