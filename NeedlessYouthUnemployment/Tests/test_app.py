from unittest import TestCase
import NeedlessYouthUnemployment.NeedlessYouthUnemployment.app as app

class TestEndpoints(TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_home(self):
        """
        Tests the 'home' endpoint
        """
        page_html = str(self.app.get('/').data)
        login_elem = 'Login'
        create_acc_elem = 'Register'
        self.assertIn(login_elem, page_html)
        self.assertIn(create_acc_elem, page_html)

    def test_login(self):
        """
        Tests the 'login' endpoint
        """
        page_html = str(self.app.get('/login').data)
        username_elem = 'Username'
        password_elem = 'Password'
        self.assertIn(username_elem, page_html)
        self.assertIn(password_elem, page_html)

    def test_register(self):
        """
        Tests the 'register' endpoint
        """
        page_html = str(self.app.get('/register').data)
        username_elem = 'Username'
        password_elem = 'Password'
        confirm_elem = 'Confirm Password'
        self.assertIn(username_elem, page_html)
        self.assertIn(password_elem, page_html)
        self.assertIn(confirm_elem, page_html)

    def test_find(self):
        """
        Test the 'find' endpoint
        """
        page_html = str(self.app.get('/find').data)
        elem = 'Find Internships'
        self.assertIn(elem, page_html)

    def test_view(self):
        """
        Test the 'view' endpoint
        """
        page_html = str(self.app.get('/view').data)
        elem = 'Your Applications'
        self.assertIn(elem, page_html)

    def test_logout(self):
        """
        Tests the 'logout' endpoint
        """
        page_html = str(self.app.get('/logout').data)
        elem = 'Redirecting...'
        self.assertIn(elem, page_html)

    # def test_add_user(self):
    #     """
    #     Tests the add_user function in db_builder
    #     """
    #     self.assertFalse(db_builder.add_user('a', 'a'))

    # def test_auth_user(self):
    #     """
    #     Tests the add_user function in db_builder
    #     """
    #     self.assertTrue(db_builder.auth_user('a', 'a'))

if __name__ == "__main__":
    unittest.main()