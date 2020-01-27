class Credential:
    """
    Class that generates new instances of credential.
    """

    credential_list = [] # Empty credential list

    def __init__(self,first_name,last_name,number,email,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        self.password = password

    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credential_list
        '''

        Credential.credential_list.append(self)


    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)


    @classmethod
    def find_by_password(cls,password):

        '''
        Method that takes in a number and returns a contact that matches that number.
        '''

        for credential in cls.credential_list:
            if credential.password == password:
                return credential


    @classmethod
    def credentials_exist(cls,password):
        '''
        Method that checks if a credential exists from the credential list.
        '''
        for credential in cls.credential_list:
            if credential.password == password:
                    return True

        return False


    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list
