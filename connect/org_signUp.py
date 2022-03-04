import mysql.connector as cd
from user_signup import signUp

con = cd.connect(host="localhost", user="root",
                 passwd="<enter password>", database="org_dat")
cursor = con.cursor()


class OrgsignUp(signUp):
    id = 1

    def __init__(self, user, num, pwd, email, address, type):
        super().__init__(
            user, num, pwd, email
        )

        self.address = address
        self.type = type

    def pushData(self):
        st = "insert into org_details values({id},'{name}',{num},'{email}','{address}','{type}')".format(
            id=id, name=self.user, num=self.num, email=self.email, address=self.address, type=self.type)
        cursor.execute(st)
        con.commit()

    def checkType():
        # checking datatypes of inputs
        pass
