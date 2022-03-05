import mysql.connector as c
import random


class services():
    cd = c.connect(host="localhost", user="root",
                   passwd="june16nevada19", database="org_dat")
    cursorO = cd.cursor()

    req_id = 0

    def __init__(self, name, request=""):
        self.name = name
        self.request = request

    def insert_requests(self, id):
        st = "insert into org_services values('{Name}','{Request}',{Status},{Request_id})".format(
            Name=self.name, Request=self.request, Status=0, Request_id=id)
        self.cursorO.execute(st)
        self.cd.commit()

    def update_status(self, status, id):
        st = "update org_services set status={Status} where request_id={Id}".format(
            Status=status, Id=id)
        self.cursorO.execute(st)
        self.cd.commit()

    def delete_request(self, id):
        st = "delete  from org_services where request_id={Request_id}".format(
            Request_id=id)
        self.cursorO.execute(st)
        self.cd.commit()

    def generate_id(self):
        self.req_id = random.randint(1, 10000)

        k = self.check_unique(self.req_id)

        if k == 1:
            self.insert_requests(self.req_id)
        else:
            self.generate_id()

    def check_unique(self, r_id):
        chq = "select * from org_services"
        self.cursorO.execute(chq)

        data = self.cursorO.fetchall()

        all_id = []
        for i in data:
            all_id.append(i[3])

        if r_id not in all_id:
            return 1
        else:
            return 0

    def add_request(self):
        self.generate_id()

    def fetch_services(self):
        qu = "select * from org_services where org_name='{Name}'".format(
            Name=self.name)
        self.cursorO.execute(qu)

        data = self.cursorO.fetchall()

        l = [["Name", "Request", "Status", "Request Id"]]

        for i in data:
            l.append(list(i))

        return l
