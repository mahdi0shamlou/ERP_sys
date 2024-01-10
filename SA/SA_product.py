from mysql.connector import connect, Error
import mysql.connector
import json
def Get_product_details(products, products_number):
    try:
        connection = mysql.connector.connect(host="localhost",
            user='root',
            password='',
            database="ERP_ACCOUNTING")
        list_lab = []
        c = 0
        for z in products:

            cursor = connection.cursor()
            sql_select_query = """select * from Accounting_product where id = %s"""
            # set variable in query
            cursor.execute(sql_select_query, (z,))
            # fetch result
            record = cursor.fetchall()

            list_lab_lab = []
            for i in range(0,len(record)):

                list_lab_lab.append(record[i][0])
                list_lab_lab.append(record[i][1])
                list_lab_lab.append(record[i][2])
                list_lab_lab.append(record[i][3])
                list_lab_lab.append(record[i][4])
                list_lab_lab.append(record[i][5])
                list_lab_lab.append(record[i][6])
                list_lab_lab.append(int(products_number[c]))
                list_lab.append(list_lab_lab)
            c = c + 1



        print(list_lab)
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return list_lab


def Get_all_product_details():
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_ACCOUNTING")
        list_lab = []
        c = 0


        cursor = connection.cursor()
        sql_select_query = """select * from Accounting_product"""
        # set variable in query
        cursor.execute(sql_select_query)
        # fetch result
        record = cursor.fetchall()

        list_lab_lab = []
        for i in range(0, len(record)):
            list_lab_lab = []
            list_lab_lab.append(record[i][0])
            list_lab_lab.append(record[i][1])
            list_lab_lab.append(record[i][2])
            list_lab_lab.append(record[i][3])
            list_lab_lab.append(record[i][4])
            list_lab_lab.append(record[i][5])
            list_lab_lab.append(record[i][6])

            list_lab.append(list_lab_lab)

        print(list_lab)
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return list_lab

