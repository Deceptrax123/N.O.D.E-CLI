import mysql.connector as c


class userProfile(c):
    dbU = c.connect(host="localhost", user="root",
                    passwd="enter_pass", database="user_det")
    cursorU = dbU.cursor()

    def __init__(self, user):
        self.user = user

    def fetch_userdetails(self):
        st = "select * from user_details where username='{user}'".format(
            user=self.user.username)
        self.cursorU.execute(st)

        dat = self.dbU.fetchall()

        return dat

    def fetch_user_requests(self):
        checker = self.check_empty()
        if checker == 1:
            st = "select * from '{name}'".format(name=self.user)
            self.cursorU.execute(st)

            dat = self.dbU.fetchall()

            l = [["id", "Service Type", "Organization Name", "Job status"]]
            for i in dat:
                l.append(list(i))
            return l
        else:
            return 0

    def check_empty(self):
        st = "select * from '{name}'".format(name=self.user)
        self.cursorU.execute(st)

        dat = self.dbU.fetchall()

        if len(dat == 0):
            return 0
        else:
            return 1

    def count_completed_task(self):
        st = "select * from '{name}' where status=1".format(name=self.user)
        self.cursorU.execute(st)

        data = self.dbU.fetchall()

        y = len(data)

        return f"Count of completed tasks is {y}"
