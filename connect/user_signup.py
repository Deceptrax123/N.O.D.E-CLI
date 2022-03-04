import time
import mysql.connector as c


class signUp(c):
    dbU = c.connect(host="localhost", user="root",
                    passwd="june16nevada19", database="user_dat")
    cursorU = dbU.cursor()

    def __init__(self, id, user, num, pwd, email, dob, doe):
        self.id = id
        self.user = user
        self.num = num
        self.pwd = pwd
        self.email = email
        self.dob = dob
        self.doe = doe

    def add_data(self):

        checker = self.checkType()
        if checker == 0:
            st = "insert into user_details values({Id},'{name}','{num}','{email}','{dob}','{doe}','{pswd}')".format(
                Id=self.id, name=self.user, num=self.num, email=self.email, dob=self.dob, doe=self.doe, pswd=self.pwd)
            self.cursorU.execute(st)
            self.dbU.commit()
            return 0
        else:
            return 1

    def check_type(self):
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

    def check_unique(self):
        # check uniqueness of username,phone no,email
        pass

    def validate(self):
        pass

    def create_user_profile(self):
        cre = "create table {Name} (id int(100),service varchar(100),org varchar(100),status int(10)".format(
            name=self.user)
        self.cursorU.execute(cre)
        self.dbU.commit()
