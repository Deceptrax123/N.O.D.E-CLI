
import mysql.connector as c


class orgsignUp():
    dbO = c.connect(host="localhost", user="root",
                    passwd="june16nevada19", database="org_dat")
    cursorO = dbO.cursor()

    def __init__(self, user, num, pwd, email, add, type):
        self.user = user
        self.num = num
        self.pwd = pwd
        self.email = email
        self.add = add
        self.type = type

    def push_data(self):
        st = "insert into org_profile values('{name}','{num}','{email}','{address}','{type}','{pwd}')".format(
             name=self.user, num=self.num, email=self.email, address=self.add, type=self.type, pwd=self.pwd)
        self.cursorO.execute(st)
        self.dbO.commit()

    def check_type(self):
        # checking datatypes of inputs
        pass
