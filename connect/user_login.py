# Individual user authentication


import mysql.connector as c


class userLogin():
    dbU = c.connect(host='localhost', user="root",
                    passwd="", database="user_dat")
    cursorU = dbU.cursor()

    que = ""

    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def check_user_name(self):
        self.que = "select * from user_details"
        self.cursorU.execute(self.que)

        data = self.cursorU.fetchall()

        names = []
        for i in data:
            names.append(i[0])

        if self.user in names:
            return 1
        else:
            return 0

    def check_password(self):
        self.que = "select * from user_details"
        self.cursorU.execute(self.que)

        data = self.cursorU.fetchall()
        pw = ""

        for i in data:
            if i[0] == self.user:
                pw = i[6]
                break
        if pw == self.pwd:
            return 1
        else:
            return 0

    def authenticate(self):
        ch1 = self.check_user_name()
        ch2 = self.check_password()

        if ch1 == 1 and ch2 == 1:
            return 1
        else:
            return 0
