import unittest # Importing the unittest module to our test project
from password import Password # Importing the Password class

class TestPassword(unittest.TestCase):
    """
    Test class that defines test cases for the passwordlock class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        test_init test case to test if the password object is initialized properly
        """
        self.new_password = Password("hidalie@gmail.com","hd2019#") # Create password object
        