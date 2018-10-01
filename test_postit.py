import unittest

class TestUserOps(unittest.TestCase):
    def test_users_can_log_in(self):
        pass

    def test_users_can_log_out(self):
        pass

    def test_for_timestamp_when_user_logs_in(self):
        pass
        
    def test_that_users_can_edit_their_own_comments(self):
        pass

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
