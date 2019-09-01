import unittest #unittest module imported
from users import Users #Importing class User from module user

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Users("firstUser", "Female", "f1924")

    def test_init(self):
          '''
          test_init test case to test if the object is initialized properly
          '''
          self.assertEqual(self.new_user.user_name, "firstUser")
          self.assertEqual(self.new_user.gender, "Female")
          self.assertEqual(self.new_user.password, "f1924")

if __name__ == '__main__':
    unittest.main()