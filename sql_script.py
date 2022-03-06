# Run before contributing to the project

import mysql.connector as c

dU = c.connect(host="localhost", user="root", passwd="")
curU = dU.cursor()


def organization_database():
    curU.execute("create database if not exists org_dat")
    dU.commit()

    curU.execute("use org_dat")

    curU.execute("Create table if not exists org_profile(org_name varchar(100),org_contactno varchar(100),org_email varchar(100),org_address varchar(100),org_type varchar(100),pwd varchar(100))")
    dU.commit()

    curU.execute(
        "Create table if not exists org_services(org_name varchar(100),request varchar(100),status int(100),request_id int(100))")
    dU.commit()


def user_database():
    curU.execute("Create database if not exists user_dat")
    dU.commit()

    curU.execute("use user_dat")

    curU.execute("create table if not exists user_details(username varchar(100),mob_num varchar(100),email varchar(100),dob date,address varchar(100),doe varchar(100),pswd varchar(100))")
    dU.commit()


organization_database()
user_database()
