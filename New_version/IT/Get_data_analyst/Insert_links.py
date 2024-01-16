from mysql.connector import connect, Error
import mysql.connector
import datetime
def insert_links_to_db_getdata(link_emalls, name, site, link_torob, link_dg):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_IT")
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO IT_getdata_list (id, name, links, link_torob, link_dg, site, type) 
                                 VALUES (%s, %s, %s, %s, %s, %s, %s) """
        x = datetime.datetime.now()
        print(x)
        record = (None, name, link_emalls, link_torob, link_dg, site, 0)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print(f"Record inserted successfully into IT_getdata_list table ---> {name} AND link is -----> {link_emalls}")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

#insert_links_to_db_getdata('https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_HP-LaserJet-Pro-M428fdn-Multifunction-Printer~id~3490637','HP M428FDN','Emalls')