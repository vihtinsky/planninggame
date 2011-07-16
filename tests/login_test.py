import base_test
import mock

class LoginTestCase(base_test.BaseTest):

    def test_login_requered(self):
        rv = self.app.get('/')
        self.assertTrue(rv.status_code!=404)
        self.assertTrue(rv.status_code==302)
        self.assertTrue('login' in rv.location)


    def test_login(self):
        rv = self.login("test")
        self.assertTrue(rv.status_code==200)


    def test_logout(self):
        self.app.get('/logout')
        self.test_login_requered()


    @mock.patch("users.User.login")
    def test_bad_login(self,mck):
        mck.return_value = False
        rv = self.app.post('/login', data=dict(
            username="bad",
            password="wrong"
        ), follow_redirects=True)
        self.assertTrue("Wrong" in rv.data)

