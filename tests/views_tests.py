import base_test

class ViewsTestCase(base_test.BaseTest):

    def test_layout(self):
        self.login("test")
        self.assertTrue(self.find_on_page("Log Out","/"))
        self.assertFalse(self.find_on_page("Admin","/"))
        self.admin_login("admin")
        self.assertTrue(self.find_on_page("Log Out","/"))
        self.assertTrue(self.find_on_page("Admin","/"))

