from mysql.connector import connect, Error
import mysql.connector
import datetime


def delet_link_data_from_db(id):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_IT")
        cursor = connection.cursor()
        # Delete a record
        sql_Delete_query = """Delete from IT_getdata_list where id = %s"""
        cursor.execute(sql_Delete_query, (id,))
        connection.commit()
        print('number of rows deleted', cursor.rowcount)
    except mysql.connector.Error as error:
        print("Failed to delete record from table: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")