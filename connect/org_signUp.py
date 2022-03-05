
from user_signup import signUp
import mysql.connector as c


class OrgsignUp(signUp, c):
    dbO = c.connect(host="localhost", user="root",
                    passwd="june16nevada19", database="org_dat")
    cursorO = dbO.cursor()

    def __init__(self, id, user, num, pwd, email, address, type):
        super().__init__(
            id, user, num, pwd, email
        )

        self.address = address
        self.type = type

    def push_data(self):
        st = "insert into org_profile values({id},'{name}',{num},'{email}','{address}','{type},'{pwd}')".format(
            id=self.id, name=self.user, num=self.num, email=self.email, address=self.address, type=self.type, pwd=self.pwd)
        self.cursorO.execute(st)
        self.dbO.commit()

    def check_type(self):
        # checking datatypes of inputs
        pass
