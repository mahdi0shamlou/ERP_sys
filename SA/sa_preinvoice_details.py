from mysql.connector import connect, Error
import mysql.connector
import json
def Get_product_details(id):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_ACCOUNTING")

        cursor = connection.cursor()
        sql_select_query = """select * from Accounting_product where id = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (id,))
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

def Get_sale_customer_details(id):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_SALE")

        cursor = connection.cursor()
        sql_select_query = """select * from Sale_coustomer where id = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (id,))
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

def Get_preinvoice_details(id):
    try:
        connection = mysql.connector.connect(host="localhost",
            user='root',
            password='',
            database="ERP_ACCOUNTING")

        cursor = connection.cursor()
        sql_select_query = """select * from Accounting_preinvoice where id = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (id,))
        # fetch result
        record = cursor.fetchall()
        list_lab = []
        list_lab_lab = []
        for i in range(0,len(record)):

            list_lab_lab.append(record[i][0])
            list_lab_lab.append(record[i][1])
            list_lab_lab.append(json.loads(record[i][2]))
            list_lab_lab.append(json.loads(record[i][3]))
            list_lab_lab.append(record[i][4])
            list_lab_lab.append(record[i][5])
            list_lab_lab.append(record[i][6])
            list_lab_lab.append(record[i][7])
            list_lab_lab.append(record[i][8])
            list_lab_lab.append(json.loads(record[i][9]))
            list_lab_lab.append(record[i][10])
            list_lab.append(list_lab_lab)
        coustomer = Get_sale_customer_details(list_lab_lab[10])

        list_lab_lab_lab = []
        for i in list_lab[0][2]:
            x=Get_product_details(i)
            list_lab_lab_lab.append(x)
        list_lab_lab.append(list_lab_lab_lab)
        list_lab_lab.append(coustomer)
        #Get_sale_customer_details()


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
#Get_preinvoice_details(1)