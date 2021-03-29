import unittest
import app


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_home(self):
        """
        Tests the 'home' endpoint
        """
        page_html = str(self.app.get('/').data)
        login_elem = '<button onclick="window.location.href=\\\'/login\\\'" class="btn w3-center w3-animate-left"> Login </button>'
        create_acc_elem = '<button onclick="window.location.href=\\\'/register\\\'" class="btn w3-center w3-animate-left"> Create Account </button>'
        self.assertIn(login_elem, page_html)
        self.assertIn(create_acc_elem, page_html)

    def test_login(self):
        """
        Tests the 'login' endpoint
        """
        page_html = str(self.app.get('/login').data)
        username_elem = '<label><strong>Username:</strong></label>\\n            <input type="text" name="User" placeholder="Username">'
        password_elem = '<label><strong>Password:</strong></label>\\n            <input type="password" name="Pass" placeholder="Password">'
        self.assertIn(username_elem, page_html)
        self.assertIn(password_elem, page_html)

    def test_register(self):
        """
        Tests the 'register' endpoint
        """
        page_html = str(self.app.get('/register').data)
        username_elem = '<label><strong>Username:</strong></label>\\n            <input type="text" name="User" placeholder="Username">'
        password_elem = '<label><strong>Password:</strong></label>\\n            <input type="password" name="Pass" placeholder="Password">'
        confirm_elem = '<label><strong>Confirm Password:</strong></label>\\n            <input type="password" name="confPass" placeholder="Password">'
        self.assertIn(username_elem, page_html)
        self.assertIn(password_elem, page_html)
        self.assertIn(confirm_elem, page_html)

    def test_logout(self):
        """
        Tests the 'logout' endpoint
        """
        page_html = str(self.app.get('/logout').data)
        elem = 'Redirecting...'
        self.assertIn(elem, page_html)
        
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
        
if __name__ == "__main__":
    unittest.main()
