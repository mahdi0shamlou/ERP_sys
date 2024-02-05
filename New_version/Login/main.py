from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from getpass import getpass
from mysql.connector import connect, Error
import mysql.connector
import datetime



def Get_password(username):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        sql_select_query = """select * from Users_users where username = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (username,))
        # fetch result
        record = cursor.fetchall()
        password = 'khali_nabashad_barayeh_logins_1238612639642149123929867'
        acc_level = -1
        path_res = 'IT'
        email_resp = 'email'
        mohr_address = '/static'
        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Email = ", row[2])
            email_resp = row[2]
            print("Phone_number  = ", row[3])
            print("Username  = ", row[4])
            print("Paswword  = ", row[5], "\n")
            password = row[5]
            acc_level = row[6]
            path_res = row[7]
            mohr_address = row[8]

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return password, acc_level, path_res, email_resp, mohr_address

def insert_log_login(id, date, user, what):
    try:
        what = 'login'
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Users_Logs (Id, Date, Who, What) 
                                VALUES (%s, %s, %s, %s) """
        x = datetime.datetime.now()
        print(x)
        record = (id, x, user, what)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
def Check_login(user, password):
    password_get, acc_level, path_res, email_resp, mohr_address = Get_password(user)
    print(password_get)
    if password == password_get:
        session['Username'] = user
        session['Password'] = password
        session['Path'] = path_res
        session['Access_level'] = acc_level
        session['email'] = email_resp
        session['mohr_address'] = mohr_address
        insert_log_login(None, '2023', user, 'login')
        return redirect('/')
    else:
        return redirect('/Login')