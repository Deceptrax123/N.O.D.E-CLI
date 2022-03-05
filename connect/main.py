# Project that centralizes all services.
from user_signup import signUp
from user_login import userLogin
from org_signUp import orgsignUp
from org_login import orgLogin
from services_provided import services


def sign_up(x):
    userName = input("Enter your user name: ")
    phoneNo = input("Enter your phone number: ")
    password = input(
        "Enter a password -> It may include letters,digits or special characters: ")
    email = input("Enter a valid email address: ")
    address = input("Enter city name and area: ")

    if x == 1:
        dob = input("enter dob in yyyy-mm-dd format: ")
        doe = input("Enter your profession: ")
        profile = signUp(userName, phoneNo, password, email, dob, address, doe)
        profile.commit_data()
        profile.create_user_profile()
    else:
        orgType = input("Enter the type of organization")
        profile = orgsignUp(userName, phoneNo, password,
                            email, address, orgType)
        profile.push_data()


def login(x):
    userName = input("Enter your username: ")
    password = input("Enter your password: ")

    k = 0
    if x == 1:
        uLogin = userLogin(userName, password)
        k = uLogin.authenticate()
    else:
        ologin = orgLogin(userName, password)
        k = ologin.authenticate()

    return k
