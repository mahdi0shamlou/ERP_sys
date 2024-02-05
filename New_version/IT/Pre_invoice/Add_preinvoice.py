from mysql.connector import connect, Error
import mysql.connector
import datetime
def Insert_into_DB_details(P_I_ID, P_ID, Count, Color, Unit, Price, Total_price, Discount_amount, Extra_amount, Tax, Invoice_net, name_p):
    pre_invoice_id = -1
    try:

        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        sql_update_query = """INSERT INTO Accounting_PreInvoice_details (id, invoice_id, product_id, count, color, unit, price, total_price, discount_amount, extra_amount, tax, invoice_net, created_at, updated_at, name_products) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        # print(str(data[5]))
        input_data = (None, P_I_ID, P_ID, Count, Color, Unit, Price, Total_price, Discount_amount, Extra_amount, Tax, Invoice_net, datetime.datetime.now(), datetime.datetime.now(), name_p)
        cursor.execute(sql_update_query, input_data)
        pre_invoice_id = cursor.lastrowid
        connection.commit()
        print(f"Record Inserted successfully {pre_invoice_id}")

    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return pre_invoice_id


def Insert_into_DB_lookup(Customer_id, User_id, Customer_name, username):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        sql_update_query = """INSERT INTO Accounting_PreInvoice_lookup (customer_id, seller_id, user_id, type, status, total_price, uploaded, seller_name, customer_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        # print(str(data[5]))
        input_data = (Customer_id, 0, username, 'IT', 0, 0, datetime.datetime.now(), 'شرکت اصلی', Customer_name)
        cursor.execute(sql_update_query, input_data)
        pre_invoice_id = cursor.lastrowid
        connection.commit()
        print(f"Record Inserted successfully {pre_invoice_id}")

    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return pre_invoice_id
def Get_product_details(ids):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        sql_select_query = ""
        sql_select_query = """select * from IT_products WHERE id = %s """
        # set variable in query
        cursor.execute(sql_select_query, (ids,))
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
            list_lab_lab.append(record[i][11])
            list_lab_lab.append(record[i][12])
            list_lab_lab.append(record[i][13])
            list_lab_lab.append(record[i][14])
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



def Add_preinvoice_IT(ID_C, products, products_number, product_name_p, product_number_p, product_price_p, username, NAME_C):
    print(NAME_C)
    P_I_ID = Insert_into_DB_lookup(ID_C, 0, NAME_C, username)
    for i in range(0,len(products)):
        P_ID = products[i]
        Count = products_number[i]
        products_de = Get_product_details(P_ID)
        name_p = products_de[0][2]
        #print(Count*products_de[0][5])
        #print(Count * products_de[0][5])
        Insert_into_DB_details(P_I_ID, P_ID, Count, 'Black', 'number', products_de[0][5], (int(Count)*int(products_de[0][5])), 0, 0, 0,0, name_p)

    for i in range(0, len(product_name_p)):
        P_ID = 0
        Count = product_number_p[i]
        Price = int(product_price_p[i])
        name_p = product_name_p[i]
        # print(Count*products_de[0][5])
        # print(Count * products_de[0][5])
        Insert_into_DB_details(P_I_ID, P_ID, Count, 'Black', 'number', Price, (int(Count) * int(Price)), 0, 0, 0, 0, name_p)
