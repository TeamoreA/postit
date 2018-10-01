import unittest
from postit import UsersOps


class TestUserOps(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.users = UsersOps()
        self.sample_user = {
            'name': 'User1',
            'password': 'password'
        }
        self.sample_comment_edit = {
            1: {
                'author': 'John',
                'message': 'Hello there!'
            }
        }

    def test_users_can_log_in(self):
        test_case = self.users.login(self.sample_user)
        self.assertIn("you are logged in", test_case)

    def test_users_can_log_out(self):
        self.assertFalse(self.users.logout())

    def test_for_timestamp_when_user_logs_in(self):
        pass

    def test_that_users_can_edit_their_own_comments(self):
        test_case = self.users.login(self.sample_comment_edit)
        self.assertIn("you are logged in", test_case)

    def test_that_users_canot_edit_other_users_comments(self):
        pass

    def test_users_cannot_delete_any_comments(self):
        pass


class TestModeratorsClass(unittest.TestCase):

    def test_moderators_can_on_edit_their_own_commands(self):
        pass

    def test_moderators_can_delete_any_comments(self):
        pass


class TestAdminClass(unittest.TestCase):

    def test_admin_can_edit_any_comments(self):
        pass

    def test_admin_can_delete_any_comments(self):
        pass


class TestComments(unittest.TestCase):

    def test_comments_contain_a_referrence_to_author(self):
        pass
