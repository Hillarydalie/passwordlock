import unittest
from credentials import User_Credentials

import pyperclip #This will help us copy paste

class TestCredentials(unittest.TestCase):
    """
    Test class that defines the testcase for user_credentials class
    """

    def setup(self):
        """
        Set up method to rum each test case
        """

        self.new_credentials = User_Credentials("Twitter", "hdn2019#")

    def test_init_(self):
        """
        test_init case to test if theobject initialised properly
        """

        self.assertEqual(self.new_credentials.account_name,"Twitter")
        self.assertEqual(self.new_credentials.account_password,"hdn2019#")

    def test_save_credentials(self):
        """
        test_save_creditials will test if the credentials objects are saved into the list_of_credentials
        """

        self.new_credentials.save_creditials() #saving new credentials object
        self.assertEqual(len(User_Credentials.list_of_credentials),1)

    def test_save_multiple_credentials(self):
        """
        test_save_multiple_credentials methods adds new multiple credentials to the list_of_credentials
        """

        self.new_credentials.save_creditials()
        test_credentials = User_Credentials("Instagram","46019hdhd") #new contact for instagram
        test_credentials.save_creditials()
        self.assertEqual(len(User_Credentials.list_of_credentials),2)

    def tearDown(self):
        """
        tearDown method does the clean up after each test case has run.
        """

        User_Credentials.list_of_credentials = []

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credential from our list of credentials
        '''
        self.new_credentials.save_credentials()
        test_credentials = User_Credentials("Instagram", "56@46019hdhd")  # new credential
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()  # Deleting a credentials object
        self.assertEqual(len(User_Credentials.list_of_credentials), 1)

    def test_find_credentials_by_name(self):
        '''
        test to check if we can find a credentials object by name and display information for the user
        '''

        self.new_credentials.save_credentials()
        test_credentials = User_Credentials("Instagram", "46019hdhd")  # new credential
        test_credentials.save_credentials()

        found_credentials = User_Credentials.find_by_name("Instagram")

        self.assertEqual(found_credentials.account_name, test_credentials.account_name)

    def test_display_all_credentials(self):
        '''
        method that returns our list of all credentials saved
        '''

        self.assertEqual(User_Credentials.display_credentials(), User_Credentials.list_of_credentials)

if __name__ == '__main__':
    unittest.main()