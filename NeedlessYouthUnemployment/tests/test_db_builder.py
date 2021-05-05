import unittest
from util import db_builder
import os


class TestDatabase(unittest.TestCase):
    def test_path(self):
        """
        Tests the path of the database
        """
        this_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__),
            '..',
            'data'))
        this_f = os.path.join(this_path, 'db.db')
        self.assertEqual(db_builder.f, this_f)

    def test_create_db(self):
        """
        Tests the create_db function in db_builder
        """
        self.assertTrue(db_builder.create_db())

    def test_add_user_already_exists(self):
        """
        Tests the add_user function in db_builder
        with a user that already exists
        """
        self.assertFalse(db_builder.add_user('a', 'a'))
    
    def test_add_user_not_exists(self):
        """
        Tests the add_user function in db_builder
        with a user that does not exist
        """
        self.assertTrue(db_builder.add_user('TEST_USER_A', 'a'))
        db_builder.remove_user('TEST_USER_A', 'a')

    def test_remove_user_already_exists(self):
        """
        Tests the remove_user function in db_builder
        with a user that already exists
        """
        db_builder.add_user('TEST_USER_A', 'a')
        self.assertTrue(db_builder.remove_user('TEST_USER_A', 'a'))
    
    def test_remove_user_not_exists(self):
        """
        Tests the remove_user function in db_builder
        with a user that does not exist
        """
        self.assertFalse(db_builder.remove_user('TEST_USER_A', 'a'))

    def test_auth_user_not_exists(self):
        """
        Tests the add_user function in db_builder
        with a user that does not exist
        """
        self.assertFalse(db_builder.auth_user('a', 'b'))

    def test_auth_user_exists(self):
        """
        Tests the add_user function in db_builder
        with a user that exists
        """
        self.assertTrue(db_builder.auth_user('a', 'a'))

    def test_add_pos(self):
        """
        Tests the add_pos function in db_builder
        """
        self.assertTrue(db_builder.add_pos('hi','a','b','c',1))

    def test_get_all_pos(self):
        """
        Tests the get_all_pos function in db_builder
        """
        pos_lst = db_builder.get_all_pos()
        self.assertTrue(len(pos_lst) >= 0)

    def test_del_pos(self):
        """
        Tests the del_pos function in db_builder
        """
        self.assertTrue(db_builder.del_pos('hi'))

    def test_add_user_app(self):
        """
        Tests the add_user_app function in db_builder
        """
        self.assertTrue(db_builder.add_user_app('a', 'hi', 'a', 'b', 'c', 1))
        self.assertFalse(db_builder.add_user_app('a', 'hi', 'a', 'b', 'c', 1))

    def test_get_user_apps(self):
        """
        Tests the get_user_apps function in db_builder
        """
        app_lst = db_builder.get_user_apps('a')
        self.assertTrue(len(app_lst) >= 0)

    def test_del_user_app(self):
        """
        Tests the del_user_app function in db_builder
        """
        self.assertTrue(db_builder.del_user_app('a', 'hi'))

if __name__ == '__main__':
    unittest.main()