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


def org_request(name):
    print("Select one of the 3 options below for type of service required")
    print("1       Add Request")
    print("2       Update Status")
    print("3       Delete Request")

    addReq = services(name, "")
    op = int(input("Enter an option : "))
    if op == 1:
        print("Choose a required volunteering service from the following options")
        print("Donation")
        print("Teaching")
        print("Medical Aid")

        choice = input("Enter one of the above options :")

        addReq = services(name, choice)
        addReq.add_request()
    elif op == 2:
        k = addReq.fetch_services()
        for i in k:
            print(i)

        print("Select the request ID for which the status needs to be updated")
        req = int(input("Enter id : "))

        print("Enter the status to be changed to 1->completed,0->Yet to be done")
        status = int(input("Enter status value : "))

        addReq.update_status(status, req)
    else:
        k = addReq.fetch_services()
        for i in k:
            print(i)

        print("Select the request ID for which the Request needs to be removed")
        req = int(input("Enter id : "))

        addReq.delete_request(req)
