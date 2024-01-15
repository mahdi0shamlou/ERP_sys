from mysql.connector import connect, Error
import mysql.connector
import datetime
print('test')
connection = mysql.connector.connect(host="78.159.108.71",
                                     user='parsot_admin',
                                     password='Q{#hZ((l}mU8',
                                     database="parsot_tjart",
                                     ssl_disabled=True)

cursor = connection.cursor()
cursor.execute('set GLOBAL max_allowed_packet=67108864')
print('test')
sql_select_query = """select * from pt_usermeta WHERE user_id = %s"""
# set variable in query
cursor.execute(sql_select_query, (1,))
