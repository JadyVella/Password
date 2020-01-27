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


if __name__ == '__main__':
    unittest.main()
