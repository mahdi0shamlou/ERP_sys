from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from getpass import getpass
from mysql.connector import connect, Error
import mysql.connector
import datetime

def list_to_strigs(list):
    strings = '['
    for i in list:
        print(i)
        strings += str(i)
        strings += ','

    strings= strings[:len(strings)-1]
    strings += ']'
    print(strings[:])
    return strings
def insert_preinvoice(id, private_id_num, list_products, customer_id, saved_by, path):
    try:
        product_codes = []
        product_number = []
        product_price = []
        price = 0
        print(list_products)
        for i in range(0,len(list_products)):
            product_codes.append(list_products[i][0])
            product_number.append(list_products[i][7])
            product_price.append(list_products[i][2])
            price += list_products[i][2]*list_products[i][7]
        product_codes = list_to_strigs(product_codes)
        product_number = list_to_strigs(product_number)
        product_price = list_to_strigs(product_price)
        print(price)
        connection = mysql.connector.connect(host="localhost",
            user='root',
            password='',
            database="ERP_ACCOUNTING")
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Accounting_preinvoice (id, id_private_num, product_codes, product_number, vrerify, verify_by, path, price, save_by, product_price, customer_id) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        x = datetime.datetime.now()
        print(x)
        record = (None, private_id_num, product_codes, product_number, 0, '', path, price, saved_by, product_price, customer_id)
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