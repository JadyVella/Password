class Credential:
    """
    Class that generates new instances of credential.
    """

    credential_list = [] # Empty credential list

    def __init__(self,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email

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
