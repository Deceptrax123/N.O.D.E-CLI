import mysql.connector as c
from org_signUp import OrgsignUp
import random

# Make changes to this file.


class Services(OrgsignUp, c):
    cd = c.connect(host="localhost", user="root",
                   passwd="enter_password", database="org_dat")
    cursorO = cd.cursor()
    req_id = 0

    def __init__(self, name, request, status):
        super().__init__(
            name
        )
        self.request = request
        self.status = status

    def add_requests(self):

        self.req_id = random.randrange(1, 100000)
        st = "insert into org_services values('{Name}',{Request}','{Status}',{Request_id})".format(
            Name=self.name, Request=self.request, Status=self.status, Request_id=self.req_id)
        self.cursorO.execute(st)
        self.cd.commit()

    def update_status(self):
        st = "update org_services set Status='{Status}'where Request_id='{Request_id}'".format(
            Status=self.status, Request_id=self.req_id)
        self.cursorO.execute(st)
        self.cd.commit()

    def delete_request(self):
        st = "delete from org_services where Request_id='{Request_id}'".format(
            Request_id=self.req_id)
        self.cursorO.execute(st)
        self.cd.commit()

    def unique_id(self):
        # run id check
        pass
