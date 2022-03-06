import mysql.connector as c


class userRequest():
    dbU = c.connect(host="localhost", user="root",
                    passwd="", database="user_dat")
    cursorU = dbU.cursor()

    dbO = c.connect(host="localhost", user="root",
                    passwd="", database="org_dat")
    cursorO = dbO.cursor()

    available_choices = []

    def __init__(self, user: str, service_choice=0):
        self.user = user
        self.service_choice = service_choice

    def check_orgs(self):
        choices = ["Teaching", "Donation", "Medical Aid"]

        choice_index = self.service_choice-1
        requested_service = choices[choice_index]

        que = "select * from org_services where request='{Request}' and status=0".format(
            Request=requested_service)
        self.cursorO.execute(que)

        results = self.cursorO.fetchall()
        if len(results) == 0:
            return "No available choices"
        else:
            self.available_choices = [
                ["Organization Name", "Service Requested", "Request Id"]]
            for i in results:
                self.available_choices.append([i[0], i[1], i[3]])

            return self.available_choices

    def update_to_profile(self, org_choice):
        qu = "insert into {name} values({id},'{type}','{org_name}',0)".format(
            name=self.user, id=org_choice[2], type=org_choice[1], org_name=org_choice[0],)
        self.cursorU.execute(qu)
        self.dbU.commit()

    def fetch_details(self, org_choice):
        qu = "select org_name,org_contactno,org_email,org_address,org_type from org_profile where org_name='{Name}'".format(
            Name=org_choice[0])
        self.cursorO.execute(qu)

        details = self.cursorO.fetchall()

        det = [["Name", "Contact Number", "Email", "Address", "Type"]]

        for i in details:
            det.append(list(i))

        return det
