import mysql.connector as c
import random


class services():
    cd = c.connect(host="localhost", user="root",
                   passwd="enter_password", database="org_dat")
    cursorO = cd.cursor()
    req_id = 0

    def __init__(self, name, request, status):
        self.name = name
        self.request = request
        self.status = status

    def insert_requests(self, Id):
        st = "insert into org_services values('{Name}',{Request}','{Status}',{Request_id})".format(
            Name=self.name, Request=self.request, Status=self.status, Request_id=Id)
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

    def generate_id(self):
        self.req_id = random.randint(1, 1000000)

        k = self.check_unique(self.req_id)

        if k == 1:
            self.insert_requests(self.req_id)
        else:
            self.generate_id()

    def check_unique(self, r_id):
        chq = "select * from org_services"
        self.cursorO.execute(chq)

        data = self.dbO.fetchall()

        all_id = []
        for i in data:
            all_id.append(i[3])

        if r_id not in all_id:
            return 1
        else:
            return 0

    def add_request(self):
        self.generate_id()
