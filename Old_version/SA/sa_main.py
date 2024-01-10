from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from getpass import getpass
from mysql.connector import connect, Error
import mysql.connector
import datetime
import json
def Get_preinvoice(Limit):
    try:
        connection = mysql.connector.connect(host="localhost",
            user='root',
            password='',
            database="ERP_ACCOUNTING")

        cursor = connection.cursor()
        sql_select_query = """select * from Accounting_preinvoice ORDER BY id DESC"""
        # set variable in query
        cursor.execute(sql_select_query)
        # fetch result
        record = cursor.fetchall()
        print(record)
        list_lab = []
        for i in range(0,len(record)):
            list_lab_lab = []
            list_lab_lab.append(record[i][0])
            list_lab_lab.append(record[i][1])
            list_lab_lab.append(json.loads(record[i][2]))
            list_lab_lab.append(json.loads(record[i][3]))
            list_lab_lab.append(record[i][4])
            list_lab_lab.append(record[i][5])
            list_lab_lab.append(record[i][6])
            list_lab_lab.append(record[i][7])
            list_lab_lab.append(record[i][8])
            list_lab.append(list_lab_lab)
        print(list_lab)
        strs = '['
        strs = strs+str(list_lab[0][2][0])
        strs = strs+']'
        print(strs)


    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return list_lab

#Get_preinvoice(1)