from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from getpass import getpass
from mysql.connector import connect, Error
import mysql.connector
import datetime
def Get_Logs(Limit):
    try:
        connection = mysql.connector.connect(host="localhost",
            user='root',
            password='',
            database="ERP_USERS")

        cursor = connection.cursor()
        sql_select_query = """select * from Users_Logs ORDER BY id DESC LIMIT 5 """
        # set variable in query
        cursor.execute(sql_select_query)
        # fetch result
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], )

            print("date = ", row[1])
            print("user = ", row[2])
            print("what = ", row[3])

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return record

