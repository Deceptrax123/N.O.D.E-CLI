import mysql.connector as c


class orgLogin(c):
    dbO = c.connect(host="localhost", user="root",
                    passwd="enter pass", database="org_data")
    cursorO = dbO.cursor()

    def __init__(self, user, pwd):
        super().__init__(
            user, pwd
        )

    def check_user_name(self):
        self.que = "select * from org_profile"
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
        self.que = "select * from org_profile"
        self.cursorU.execute(self.que)

        data = self.dbU.fetchall()
        pw = ""

        for i in data:
            if i[1] == self.user:
                pw = i[6]
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
