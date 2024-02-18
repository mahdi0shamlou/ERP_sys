from mysql.connector import connect, Error
import mysql.connector

def Insert_Product_acc_in_db(name, desck, price, number):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Accounting_Product_details (`id`, `name`, `price`, `number`, `describe`, `type`, `path`) VALUES (%s, %s, %s, %s, %s, %s, %s)"""


        record = (None, name, price, number, desck, 0, 'ACC')
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into Accounting_Product_details table")



    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
def Delet_Product_acc_in_db(id):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")
        cursor = connection.cursor()
        mySql_insert_query = """DELETE FROM Accounting_Product_details WHERE id = %s"""
        record = (id,)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into Accounting_Product_details table")
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

