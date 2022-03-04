import mysql.connector as c

dbU = c.connect(host="localhost", user="root",
                passwd="june16nevada19", database="user_dat")
cursorU = dbU.cursor()

dbO = c.connect(host="localhost", user="root",
                passwd="june16nevada19", database="org_dat")
cursorO = dbO.cursor()

cursorU.execute("select * from user_details")
cursorO.execute("select * from org_profile")
