import mysql.connector as c
from user_signup import signUp


class userRequest(signUp, c):
    dbU = c.connect(host="localhost", user="root",
                    passwd="<enter_password>", database="user_dat")
    cursorU = dbU.cursor()

    dbO = c.connect(host="localhost", user="root",
                    passwd="enter_password", database="org_dat")
    cursorO = dbO.cursor()

    available_choices = []

    def __init__(self, user, service_choice):
        super().__init__(
            user
        )
        self.service_choice = service_choice

    def check_orgs(self):
        choices = ["Teaching", "Donation", "Medical Assistance"]

        choice_index = self.service_choice-1
        requested_service = choices[choice_index]

        que = "select * from org_services where request='{Request}'".format(
            Request=requested_service)
        self.cursorO.execute(que)

        results = self.cursorO.fetchall()

        for i in results:
            if i not in self.available_choices:
                self.available_choices.append([i[0], i[3]])

        return self.available_choices

    def update_to_profile(self, org_choice):
        qu = "insert into {name} values('{org_name}','{Type}',0,{id})".format(
            name=self.user, org_name=org_choice[0], id=org_choice[1])
        self.cursorU.execute(qu)
        self.dbU.commit()

    def fetch_details(self, org_choice):
        qu = "select * from org_profile where org_name={Name}".format(
            Name=org_choice[0])
        self.dbO.execute(qu)

        details = self.dbO.fetchall()

        return details