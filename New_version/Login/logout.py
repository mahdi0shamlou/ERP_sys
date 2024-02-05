from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from getpass import getpass
from mysql.connector import connect, Error
import mysql.connector
import datetime


def insert_log_login_logout(id, date, user, what):
    try:
        what = 'logout'
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