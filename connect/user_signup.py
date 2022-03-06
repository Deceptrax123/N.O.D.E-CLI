# User sign-up

import mysql.connector as c


class signUp():
    dbU = c.connect(host="localhost", user="root",
                    passwd="", database="user_dat")
    cursorU = dbU.cursor()

    def __init__(self, user, num, pwd, email, dob, add, doe):
        self.user = user
        self.num = num
        self.pwd = pwd
        self.email = email
        self.dob = dob
        self.doe = doe
        self.add = add

    def commit_data(self):
        st = "insert into user_details values('{name}','{num}','{email}','{dob}','{add}','{doe}','{pswd}')".format(
            name=self.user, num=self.num, email=self.email, dob=self.dob, add=self.add, doe=self.doe, pswd=self.pwd)
        self.cursorU.execute(st)
        self.dbU.commit()

    def create_user_profile(self):
        cre = "create table {Name} (id int(100),service varchar(100),org varchar(100),status int(10))".format(
            Name=self.user)
        self.cursorU.execute(cre)
        self.dbU.commit()
