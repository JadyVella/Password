#!/usr/bin/env python3.7
from user import User
from credentials import Credential


def create_credentials(fname,lname,phone,email,pwd):
    '''
    Function to create a new credentials
    '''

    new_credentials = Credential(fname,lname,phone,email,pwd)
    return new_credentials


def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()


def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()


def find_credentials(pwd):
    '''
    Function that finds a contact by password and returns the credentials
    '''
    return Credential.find_by_password(pwd)


def check_existing_credentials(pwd):
    '''
    Function that check if a credentials exists with that password and return a Boolean
    '''
    return Credential.credentials_exist(pwd)


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()


def main():
    print("Hello you are welcomed in our Password finder application. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new account, dc - display credentials, fc -find a credentials, ex -exit the credentials list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Credential")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()

                            print("Password ...")
                            pwd = input()


                            save_credentials(create_credentials(f_name,l_name,p_number,e_address,pwd))
                            print ('\n')
                            print(f"New Credential {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your credentials")
                                    print('\n')

                                    for credentials in display_credentials():
                                            print(f"{credentials.first_name} {credentials.last_name} .....{credentials.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the password")

                            search_password = input()
                            if check_existing_credentials(search_password):
                                    search_credentials = find_credentials(search_password)
                                    print(f"{search_credentials.first_name} {search_credentials.last_name}")
                                    print('-' * 20)

                                    print(f"Password.......{search_credentials.password}")
                                    print(f"Email address.......{search_credentials.email}")
                            else:
                                    print("That credential does not exist")

                    elif short_code == "ex":
                            print("Thank you for your attempt")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
