from mysql.connector import connect, Error
import mysql.connector
import datetime

connection = mysql.connector.connect(host="185.94.96.98",
                                     user='parso_bazrgani',
                                     password='S{VN^7kOIP7F',
                                     database="parso_tjart")

cursor = connection.cursor()

sql_select_query = """select * from pt_wc_order_product_lookup WHERE customer_id = %s"""
# set variable in query
cursor.execute(sql_select_query, (4,))
record = cursor.fetchall()
print(record)
