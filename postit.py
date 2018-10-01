""" Postit.py 
all_comments = {
    int : {
        "author" : str,
        "message" : str,
        "datetime" : str
    }
}
"""
import datetime

all_posts = {}

class UsersOps():
    def __init__(self):
        self.login_status = False
        self.logged_in_at = None      

    def login(self, username, password):
        # simple regex

        self.login_status = True
        self.logged_in_at = datetime.datetime.now()
        print('YOU ARE LOGGED IN')

    
    def logout(self):
        pass

    def post_comment(self):
        pass
    
    def edit_own_comment(self):
        pass



class ModeratorOps(UsersOps):
    pass

class AdminOps(ModeratorOps):
    pass

def main():
    new_username = input('Enter username :')
    new_password = input('Enter password :')

    samle_user = UsersOps()
    samle_user.login(new_username, new_password)


if __name__ == '__main__':
    main()