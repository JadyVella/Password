import unittest
from credentials import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_credentials = Credential("Felix","Ouma","0712345678","felix@ms.com")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.first_name,"Felix")
        self.assertEqual(self.new_credentials.last_name,"Ouma")
        self.assertEqual(self.new_credentials.phone_number,"0712345678")
        self.assertEqual(self.new_credentials.email,"felix@ms.com")


    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credential list
        '''
        
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credential.credential_list),1)


    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials objects to our credential_list
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credential("Test","user","0712345678","test@user.com")
        test_credentials.save_credentials()
        self.assertEqual(len(Credential.credential_list),2)


    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credential("Test","user","0712345678","test@user.com")
        test_credentials.save_credentials()

        self.new_credentials.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)


if __name__ == '__main__':
    unittest.main()
