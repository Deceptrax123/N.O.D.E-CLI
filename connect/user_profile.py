import mysql.connector as c


class userProfile():
    dbU = c.connect(host="localhost", user="root",
                    passwd="", database="user_dat")
    cursorU = dbU.cursor()

    def __init__(self, user):
        self.user = user

    def fetch_userdetails(self):
        st = "select username,mob_num,email,dob,address,doe from user_details where username='{user}'".format(
            user=self.user)
        self.cursorU.execute(st)

        dat = self.cursorU.fetchall()

        l = list()
        for i in dat:
            l = list(i)

        return l

    def fetch_user_requests(self):
        checker = self.check_empty()
        if checker == 1:
            st = "select * from {name}".format(name=self.user)
            self.cursorU.execute(st)

            dat = self.cursorU.fetchall()

            l = [["id", "Service Type", "Organization Name", "Task status"]]
            for i in dat:
                l.append(list(i))
            return l
        else:
            return 0

    def check_empty(self):
        st = "select * from {name}".format(name=self.user)
        self.cursorU.execute(st)

        dat = self.cursorU.fetchall()

        if len(dat) == 0:
            return 0
        else:
            return 1

    def count_completed_task(self):
        st = "select * from {name} where status=1".format(name=self.user)
        self.cursorU.execute(st)

        data = self.cursorU.fetchall()

        y = len(data)

        return y
