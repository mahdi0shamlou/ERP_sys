from mysql.connector import connect, Error
import mysql.connector
import json
def Get_all_sale_customer_details(id):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_SALE")

        cursor = connection.cursor()
        sql_select_query = """select * from Sale_coustomer"""
        # set variable in query
        cursor.execute(sql_select_query)
        # fetch result
        record = cursor.fetchall()
        list_lab = []
        for i in range(0, len(record)):
            list_lab_lab = []
            list_lab_lab.append(record[i][0])
            list_lab_lab.append(record[i][1])
            list_lab_lab.append(record[i][2])
            list_lab_lab.append(record[i][3])
            list_lab_lab.append(record[i][4])
            list_lab_lab.append(record[i][5])
            list_lab_lab.append(record[i][6])
            list_lab_lab.append(record[i][7])
            list_lab_lab.append(record[i][8])
            list_lab_lab.append(record[i][9])
            list_lab_lab.append(record[i][10])
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


#x = Get_all_sale_customer_details(0)