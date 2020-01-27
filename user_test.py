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


#     def tearDown(self):
#         '''
#         tearDown method that does clean up after each test case has run.
#         '''

#         User.user_list = []
    
     def test_save_multiple_user(self):
#         '''
#         test_save_multiple_user to test if we can save a variety of user objects to the user_list
#         '''

#         self.new_user.save_user()
#         test_user = User("Test", "password")
#         test_user.save_user()
#         self.assertEqual(len(User.user_list),2)


# if __name__ == '__main__':
#     unittest.main()
