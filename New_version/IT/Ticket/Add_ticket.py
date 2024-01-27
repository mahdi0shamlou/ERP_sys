from mysql.connector import connect, Error
import mysql.connector
import json
import datetime
def Add_tickets_IT(subject, section_to, username, section_from):
    pre_id = 0
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_USERS")
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Users_ticket (id, `from`, `to`, desck, date, section_from, section_to, is_read, status, is_finish, is_new) 
                                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        date_time = datetime.datetime.now()

        record = (None, username, '', subject, date_time, section_from, section_to, 0, 'تعیین نشده', 0, 0)
        cursor.execute(mySql_insert_query, record)
        pre_id = cursor.lastrowid
        connection.commit()
        print(f"Record inserted successfully into IT_products table ---> {username}")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return pre_id
def Add_message_IT(desck, pre_id, username, section_from):

    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_USERS")
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO User_ticket_messange (id, ticket_id, messange, date, is_read, is_changed, is_delet, user_send, who_send) 
                                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """
        date_time = datetime.datetime.now()

        record = (None, pre_id, desck, date_time, 0, 0, 0, username, section_from)
        cursor.execute(mySql_insert_query, record)
        pre_id = cursor.lastrowid
        connection.commit()
        print(f"Record inserted successfully into IT_products table ---> {username}")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return pre_id

def Add_status_IT(desck, pre_id):
    if desck == '1':
        desck = 'انجام شده'
    if desck == '-1':
        desck = 'رد شده'
    if desck == '0':
        desck = 'در دست اقدام'
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_USERS")
        cursor = connection.cursor()
        mySql_insert_query = """Update Users_ticket set status = %s where id = %s"""
        date_time = datetime.datetime.now()

        record = (desck, pre_id,)
        cursor.execute(mySql_insert_query, record)

        connection.commit()
        print(f"Record inserted successfully into IT_products table ---> {desck}")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return pre_id

def start(subject, desck, section_to, username, section_from):
    pre_id = Add_tickets_IT(subject, section_to, username, section_from)
    pre_id = Add_message_IT(desck, pre_id, username, section_from)
    print('inserted')