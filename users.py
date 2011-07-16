import db
import settings


class User(object):
    """Used for admin users also"""
    username = None
    password_hash = None
    _is_admin = None
    cli = None

    def __init__(self, username, password_hash='', is_admin=False):
        self.cli = db.Db().client
        self.username = username
        self.password_hash = password_hash
        self._is_admin = is_admin
        self.key = "%s-%s-%s" % (
            settings.REDIS_PREFIX, self.__class__.__name__,
            self.username
        )
        self.admin_key = "%s-admins-%s" % (settings.REDIS_PREFIX, self.username)

    def save(self):
        self.cli.set(self.key, self.password_hash)

        if self._is_admin:
            self.cli.set(self.admin_key, self.username)
        else:
            self.cli.delete(self.admin_key)

    def login(self):
        ph = self.cli.get(self.key)
        if ph == self.password_hash:
            return self.username, self.__check_admin()
        else:
            return False

    def __check_admin(self):
        return  self.cli.get(self.admin_key)!=None
