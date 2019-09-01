class User_Credentials:
    """
    Class that generates new instances of user credentials for their accounts
    """

    list of credentials = [] #Empty user credentials list

    def __init__(self, account_name, account_password):
        self.account_name = account_name
        self.account_password = account_password

    def save_credentials(self):
        """
        Save credentials methods that stores new credentials into the list_of_credentials
        """

        self.list_of_credentials.append(self)

    def delete_credentials(self):
        '''
        delete_contact method deletes a saved credential from the list_of_creds
        '''

        User_Credentials.list_of_creds.remove(self)

    @classmethod
    def find_by_name(cls, account_name):
        '''
        Method that takes in a name and returns a credential that matches that number.

        Args:
            name: account_name to search for
        Returns :
            The account_name and its password
        '''

        for credential in cls.list_of_credentials:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.list_of_credentials
