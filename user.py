class User:

    """
    Class that generates new instances of users.
    """


    user_list = [] # Empty user list

    def __init__(self,login_username,password):

        # docstring removed for simplicity

        self.login_username = login_username
        self.password = password


    def save_user(self):
        '''
        save_user method saves user into the list
        '''

        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user deletes user that is saved in the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_password(cls,password):
        '''
        Method that takes in password and display the user that matches the password
        '''

        for user in cls.user_list:
            if user.password == password:
                return user

    @classmethod
    def user_exist(cls,password):
        '''
        Method that checks if the user exist in the user_list
        '''

        for user in cls.user_list:
            if user.password == password:
                return True

        
        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''

        return cls.user_list







    


    