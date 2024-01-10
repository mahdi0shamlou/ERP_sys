from mysql.connector import connect, Error
import mysql.connector
import json
def Preinvoice_delet(id):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_ACCOUNTING")
        cursor = connection.cursor()
        # Delete a record
        sql_Delete_query = """Delete from Accounting_preinvoice where id = %s"""
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