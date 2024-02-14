from mysql.connector import connect, Error
import mysql.connector
import datetime
def Insert_cutomer_SA(data):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Sale_Coustomer (id, name, economic_code, national_id, address, postal_code, state, city, phone_number, type, path) 
                                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        x = datetime.datetime.now()
        print(x)
        record = (None, data[1], data[3], data[2], data[5], data[4], 0, 0, data[0], 0, 'SA')
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print(f"Record inserted successfully into IT_products table ---> {data[2]}")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")