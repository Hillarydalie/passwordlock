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
        test_credentials = User_Credentials("Instagram","46#2019hd") #new contact for instagram
        test_credentials.save_creditials()
        self.assertEqual(len(User_Credentials.list_of_credentials),2)

    def tearDown(self):
        """
        tearDown method does the clean up after each test case has run.
        """

        User_Credentials.list_of_credentials = []

    def delete_credentials(self):
        '''
        delete_contact method deletes a saved credential from the list_of_credentials
        '''

        User_Credentials.list_of_credentials.remove(self)

    
