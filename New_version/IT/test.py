from mysql.connector import connect, Error
import mysql.connector
import datetime
#https://api.torob.com/v4/base-product/price-chart/?prk=826600ed-b0f4-4928-9d81-b05b2c236c2f&t=1706702051007&source=next_desktop
'''
Host: api.torob.com

User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0

Accept: */*

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate, br

Referer: https://torob.com/

Origin: https://torob.com

Connection: keep-alive

Cookie: is_torob_user_logged_in=True; search_session=xftvbuxtryfdgnefjnqhhcnsaflcnppx; _gcl_au=1.1.53083946.1706701973; _ga_CF4KGKM3PG=GS1.1.1706701973.1.1.1706702050.60.0.0; _ga=GA1.2.72549834.1706701973; _clck=1wjiors%7C2%7Cfiv%7C0%7C1491; _gid=GA1.2.415493717.1706701974; _ym_uid=1706701975614627935; _ym_d=1706701975; _ym_isad=2; _ym_visorc=b; _clsk=m4yovc%7C1706702002335%7C2%7C0%7Ct.clarity.ms%2Fcollect; _gat_UA-105982196-1=1

Sec-Fetch-Dest: empty

Sec-Fetch-Mode: cors

Sec-Fetch-Site: same-site

'''
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
