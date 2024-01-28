from mysql.connector import connect, Error
import mysql.connector

def Send_invoice_to_sended(id):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_ACCOUNTING")

        cursor = connection.cursor()
        sql_update_query = """Update Accounting_Factors_lookup set status = 1 where id = %s"""
        # print(str(data[5]))
        input_data = (id,)
        cursor.execute(sql_update_query, input_data)
        connection.commit()
        print(f"Record Updated successfully {id}")

    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
def Send_invoice_to_sended_status_backe(id):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_ACCOUNTING")

        cursor = connection.cursor()
        sql_update_query = """Update Accounting_Factors_lookup set status = 2 where id = %s"""
        # print(str(data[5]))
        input_data = (id,)
        cursor.execute(sql_update_query, input_data)
        connection.commit()
        print(f"Record Updated successfully {id}")

    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
def Send_invoice_to_sended_status_remove(id):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_ACCOUNTING")

        cursor = connection.cursor()
        sql_update_query = """Update Accounting_Factors_lookup set status = 3 where id = %s"""
        # print(str(data[5]))
        input_data = (id,)
        cursor.execute(sql_update_query, input_data)
        connection.commit()
        print(f"Record Updated successfully {id}")

    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
def Send_invoice_to_sended_status_okay(id):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_ACCOUNTING")

        cursor = connection.cursor()
        sql_update_query = """Update Accounting_Factors_lookup set status = 4 where id = %s"""
        # print(str(data[5]))
        input_data = (id,)
        cursor.execute(sql_update_query, input_data)
        connection.commit()
        print(f"Record Updated successfully {id}")

    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")