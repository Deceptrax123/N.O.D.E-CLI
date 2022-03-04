import mysql.connector as c
import time

con = c.connect(host="localhost", user="root",
                passwd="june16nevada19", database="user_dat")
cursor = con.cursor()


class signUp():
    id = 1

    def __init_(self, user, num, pwd, email, dob, doe):
        self.user = user
        self.num = num
        self.pwd = pwd
        self.email = email
        self.dob = dob
        self.doe = doe

    def addData(self):

        checker = self.checkType()
        if checker == 0:
            st = "insert into user_details values({Id},'{name}','{num}','{email}','{dob}','{doe}','{pswd}')".format(
                Id=id, name=self.name, num=self.num, email=self.email, dob=self.dob, doe=self.doe, pswd=self.pwd)
            cursor.execute(st)

            id += 1

    def checkType(self):
        r1 = isinstance(self.doe, str)
        r2 = isinstance(self.user, str)
        r3 = isinstance(self.pwd, str)
        r4 = isinstance(self.dob, str)
        r5 = isinstance(self.email, str)

        validation = [r1, r2, r3, r4, r5]

        ch = 0
        for i in validation:
            if not i:
                ch = 1
                break
        if(ch == 1):
            print("Invalid entry, try again")
            time.sleep(2)
            self.addData()
        else:
            return 0

    def checkUnique(self):
        # check uniqueness of username,phone no,email
        return 0
