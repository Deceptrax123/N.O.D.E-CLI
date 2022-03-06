# Organization user authentication

import mysql.connector as c


class orgLogin():
    dbO = c.connect(host="localhost", user="root",
                    passwd="", database="org_dat")
    cursorO = dbO.cursor()

    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def check_user_name(self):
        self.que = "select * from org_profile"
        self.cursorO.execute(self.que)

        data = self.cursorO.fetchall()

        names = []
        for i in data:
            names.append(i[0])

        if self.user in names:
            return 1
        else:
            return 0

    def check_password(self):
        self.que = "select * from org_profile"
        self.cursorO.execute(self.que)

        data = self.cursorO.fetchall()
        pw = ""

        for i in data:
            if i[0] == self.user:
                pw = i[5]
                break
        if pw == self.pwd:
            return 1
        else:
            return 0

    def authenticate(self):
        ch1 = self.check_password()
        ch2 = self.check_user_name()

        if ch1 == 1 and ch2 == 1:
            return 1
        else:
            return 0
