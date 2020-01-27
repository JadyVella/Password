import unittest
from user import User

class TestUser(unittest.TestCase):
     '''
     Test class that defines test cases for the User class behaviour

     Args:
         unittest.Testcase: TestCase class that helps in creating test cases
     '''

     def setUp(self):
         '''
         Set up method to run before each test cases.
         '''

         self.new_user = User("Jady","SecretKey")


     def test_init(self):
         '''
         test_init test case to test if the object is properly initialized
         '''

         self.assertEqual(self.new_user.login_username,"Jady")
         self.assertEqual(self.new_user.password,"SecretKey")

    
     def test_save_user(self):
         '''
         test_save_user test case to test if user object can be saved into the user list
         '''

         self.new_user.save_user()
         self.assertEqual(len(User.user_list),1)


     def tearDown(self):
         '''
         tearDown method that does clean up after each test case has run.
         '''

         User.user_list = []
    
     def test_save_multiple_user(self):
         '''
         test_save_multiple_user to test if we can save a variety of user objects to the user_list
         '''

         self.new_user.save_user()
         test_user = User("Jady", "ScretKey")
         test_user.save_user()
         self.assertEqual(len(User.user_list),2)

     def test_delete_user(self):
         '''
         test_delete_user to test if we can remove user from a user_list
         '''

         self.new_user.save_user()
         test_user = User("Jady", "SecretKey")
         test_user.save_user()

         self.new_user.delete_user()
         self.assertEqual(len(User.user_list),1)

     def test_find_user_by_password(self):
         '''
         Test to see if we can find a user by password and display information
         '''

         self.new_user.save_user()
         test_user = User("Jady", "SecretKey")
         test_user.save_user()

         found_user = User.find_by_password("SecretKey")

         self.assertEqual(found_user.login_username, test_user.login_username)

     def test_user_exists(self):
         '''
         test to check if we can return a boolean if user doesn't exist
         '''

         self.new_user.save_user()
         test_user = User("Jady", "SecretKey")
         test_user.save_user()

         user_exists = User.user_exist("SecretKey")

         self.assertTrue(user_exists)

     def test_display_all_users(self):
         '''
         method that returns a list of all users saved
         '''

         self.assertEqual(User.display_users(),User.user_list)



    


if __name__ == '__main__':
     unittest.main()
