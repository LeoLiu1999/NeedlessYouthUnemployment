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

    def test_add_user(self):
        """
        Tests the add_user function in db_builder
        """
        self.assertFalse(db_builder.add_user('a', 'a'))

    def test_auth_user(self):
        """
        Tests the add_user function in db_builder
        """
        self.assertTrue(db_builder.auth_user('a', 'a'))

if __name__ == '__main__':
    unittest.main()