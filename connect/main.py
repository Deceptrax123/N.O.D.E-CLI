# Run this module for testing.


from user_signup import signUp
from user_login import userLogin
from org_signUp import orgsignUp
from org_login import orgLogin
from services_provided import services
from user_requests import userRequest
from user_profile import userProfile


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

    return k, userName


def org_request(name):
    print("Select one of the 3 options below for type of service required")
    print("1       Add Request")
    print("2       Update Status")
    print("3       Delete Request")
    print()
    addReq = services(name, "")
    op = int(input("Enter an option : "))
    print()
    if op == 1:
        print("Choose a required volunteering service from the following options")
        print("Donation")
        print("Teaching")
        print("Medical Aid")
        print()

        choice = input("Enter one of the above options :")

        addReq = services(name, choice)
        addReq.add_request()

        print("Request added, your request will be available to all users")
    elif op == 2:
        k = addReq.fetch_services()
        for i in k:
            print(i)

        print("Select the request ID for which the status needs to be updated")
        req = int(input("Enter id : "))

        print()
        print("Enter the status to be changed : 1->completed,0->Yet to be done")
        status = int(input("Enter status value : "))

        print()
        addReq.update_status(status, req)

        print("Status updated")
    else:
        k = addReq.fetch_services()
        for i in k:
            print(i)
        print()
        print("Select the request ID for which the Request needs to be removed")
        req = int(input("Enter id : "))

        addReq.delete_request(req)

        print("Request deleted")


def user_request(name):
    print("Select one of the below available volunteering activities which you are interested in")
    print("1      Teaching")
    print("2      Donations")
    print("3      Medical Aid")

    op = int(input("Select an option : "))
    print()
    print("Checking for organizations that require the selected volunteering service.....")

    req = userRequest(name, op)

    available = req.check_orgs()

    if available == "No available choices":
        print("There are no available volunteering oppurtunities as per request")
    else:
        for item in available:
            print(list(item))
        print()
        print("Select the choice of volunteering service that you would like to work")

        cho = int(input("Enter an option : "))

        selected_service = available[cho]
        print("Would you like to continue with the same organization")
        y = int(input("Enter 1 for yes and 2 for no"))

        if y == 1:
            req.update_to_profile(selected_service)

            print("Fetching details of the Organization for further communication....")
            print("Details  added to your profile....")
            print()
            det = req.fetch_details(selected_service)

            for k in det:
                print(k)
        else:
            user_request(name)


def user_profile(name):
    print(f"Profile of {name}")
    print("User details section: ")
    print()
    profile = userProfile(name)

    userDetails = profile.fetch_userdetails()

    l1 = ["Name", "Mobile number", "Email",
          "Date of Birth", "Address", "Profession"]
    l2 = list()
    for i in userDetails:
        l2.append(i)

    for k in range(0, len(l1)):
        print(f"{l1[k]}------->{l2[k]}")
    print()
    print(f"{name} Volunteering Stats")
    print()
    volunteering = profile.fetch_user_requests()

    if volunteering == 0:
        print("Currently No requests have been made or completed.")
    else:
        for j in volunteering:
            print(j)

        count = profile.count_completed_task()
        print()
        print(f"The count of completed volunteering tasks is {count}")


print("------------------N.O.D.E-----------------")
print("------A UNIFIED NETWORK TO DELIVER AID------")
print("-------------------------------------------")

cont = 0
while(cont != 2):
    print("Press 1 for indvidual use and press 2 for organization : ")

    type = int(input("Enter an option based on the above prompt :"))
    print()
    print("Select one of the two options")
    print("1--------->Login for existing users")
    print("2--------->Signup for new users")
    print()
    log = int(input("Enter an option based on the above prompt"))

    if log == 1:
        y = login(type)

        r, uName = y
        if r == 1:
            print("Login successful")

            print(f"Welcome {uName} to N.O.D.E.")
            print("Choose what you would like to do next")
            print("----------------")
            print()
            if type == 1:
                opt = 0
                while opt != 3:
                    print("1------- View profile")
                    print("2------- Apply for a volunteering service")
                    print("3------- Sign out")

                    opt = int(input("Enter an option"))

                    if(opt == 1):
                        user_profile(uName)
                        print("-------")
                    elif opt == 2:
                        user_request(uName)
                        print("-------")
                    elif opt == 3:
                        print("Thank you for using NODE")
                        print("Signing Out....")
            elif type == 2:
                print("You may add a request for volunteering and view current requests")
                opt = 0
                while opt != 2:
                    print("Press 1 to make requests and 2 to signout")
                    opt = int(input("Enter an option : "))
                    print()
                    if opt != 2:
                        org_request(uName)
                    else:
                        print("Thank you for using NODE")
                        print("Signing Out...")
        else:
            print("Invalid Credentials try again")
    elif log == 2:
        sign_up(type)
        print("Successful sign up, you may now log in using the same credentials")

    print("Press 1 to continue and press 2 to close the app....")
    cont = int(input("Enter a value based on above prompt : "))
