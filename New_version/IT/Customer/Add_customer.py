from mysql.connector import connect, Error
import mysql.connector
import datetime
def Insert_g_cutomer(data, N_id, address):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO IT_customers (id, customer_id, user_id, username, first_name, last_name, email, date_last_active, date_registered, country, postcode, city, state, national_id, address) 
                                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        x = datetime.datetime.now()
        print(x)
        record = (
        None, data[0], data[1], data[2], data[3], data[4], data[5], 0, 0, 0, data[7], data[6],
        0, N_id, address)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print(f"Record inserted successfully into IT_products table ---> {N_id}")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")