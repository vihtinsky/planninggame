import game
import mock
import unittest

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = game.app.test_client()

    @mock.patch("users.User.login")
    def login(self, username, mck):
        mck.return_value = "test", False
        return self.app.post('/login', data=dict(
            username=username,
            password="password"
        ), follow_redirects=True)


    @mock.patch("users.User.login")
    def admin_login(self, username, mck):
        mck.return_value = "test", True
        return self.app.post('/login', data=dict(
            username=username,
            password="password"
        ), follow_redirects=True)

    def find_on_page(self, text, url):
        rv = self.app.get(url)
        return (text in rv.data)
