import mysql.connector as c


class userLogin(c):
    dbU = c.connect(host='localhost', user="root",
                    passwd="enter_pass", database="user_data")
    cursorU = dbU.cursor()

    que = ""

    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def check_user_name(self):
        self.que = "select * from user_details"
        self.cursorU.execute(self.que)

        data = self.dbU.fetchall()

        names = []
        for i in data:
            names.append(i[1])

        if self.user in names:
            return 1
        else:
            return 0

    def check_password(self):
        self.que = "select * from user_details"
        self.cursorU.execute(self.que)

        data = self.dbU.fetchall()
        pw = ""

        for i in data:
            if i[1] == self.user:
                pw = i[7]
                break
        if pw == self.pwd:
            return 1
        else:
            return 0

    def authenticate(self):
        ch1 = self.check_password()
        ch2 = self.check_user_name()

        if ch1 == 1 and ch2 == 0:
            return 1
        else:
            return 0
