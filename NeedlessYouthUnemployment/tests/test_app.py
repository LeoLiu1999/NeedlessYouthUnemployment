import unittest
import app


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_home_not_logged_in(self):
        """
        Tests the 'home' endpoint while not logged in
        """
        page_html = str(self.app.get('/').data)
        login_elem = 'Login'
        create_acc_elem = 'Register'
        self.assertIn(login_elem, page_html)
        self.assertIn(create_acc_elem, page_html)

    def test_home_logged_in(self):
        """
        Tests the 'home' endpoint while logged in
        """
        self.app.post('/auth', data=dict(Username="a", Password="a"))
        page_html = str(self.app.get('/').data)
        find_elem = 'Find'
        view_elem = 'View'
        logout_elem = 'Logout'
        self.assertIn(find_elem, page_html)
        self.assertIn(view_elem, page_html)
        self.assertIn(logout_elem, page_html)

    def test_login_not_logged_in(self):
        """
        Tests the 'login' endpoint while not logged in
        """
        page_html = str(self.app.get('/login').data)
        username_elem = 'Username'
        password_elem = 'Password'
        self.assertIn(username_elem, page_html)
        self.assertIn(password_elem, page_html)

    def test_login_logged_in(self):
        """
        Tests the 'login' endpoint while logged in
        """
        self.app.post('/auth', data=dict(Username="a", Password="a"))
        page_html = str(self.app.get('/login').data)
        find_elem = 'Find'
        view_elem = 'View'
        logout_elem = 'Logout'
        self.assertIn(find_elem, page_html)
        self.assertIn(view_elem, page_html)
        self.assertIn(logout_elem, page_html)

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

    def test_signup_no_match_pw(self):
        """
        Tests the 'signup' endpoint
        """
        response = self.app.post('/signup',
                                 data=dict(Username="newa",
                                           Password="newa",
                                           ConfirmPassword="newb"),
                                 follow_redirects=True)

        assert b'2 passwords that you entered' in response.data

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


if __name__ == "__main__":
    unittest.main()
