from mysql.connector import connect, Error
import mysql.connector
import datetime


connection = mysql.connector.connect(host="localhost",
                                         user='root',
                                         password='ya mahdi',
                                         database="ERP_USERS")

cursor = connection.cursor()

sql_select_query = """select * from Users_Logs"""
# set variable in query
cursor.execute(sql_select_query)
record = cursor.fetchall()
print(record)
