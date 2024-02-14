from mysql.connector import connect, Error
import mysql.connector
def Delet_Customer_SA(id):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        # Delete a record
        sql_Delete_query = """Delete from Sale_Coustomer where id = %s"""
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