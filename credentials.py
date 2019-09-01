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