from mysql.connector import connect, Error
import mysql.connector
import datetime

from orca.orca import start


def Select_name_products_from_db(id):
    verifyes_x = 0
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_IT")
        cursor = connection.cursor()
        sql_select_query = """select * from IT_products where product_id=%s"""
        # set variable in query
        cursor.execute(sql_select_query,(id,))
        # fetch result
        record = cursor.fetchall()

        list_lab = []
        for i in range(0, len(record)):
            verifyes_x = 1
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


            list_lab.append(list_lab_lab)
        print(list_lab)


    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            if verifyes_x == 1:
                print(verifyes_x)
                return list_lab[0][2]
            else:
                return 0
def Select_name_customer_from_db(id):
    verifyes_x = 0
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_IT")
        cursor = connection.cursor()
        sql_select_query = """select * from IT_customers where user_id=%s"""
        # set variable in query
        cursor.execute(sql_select_query,(id,))
        # fetch result
        record = cursor.fetchall()

        list_lab = []
        for i in range(0, len(record)):
            verifyes_x = 1
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


            list_lab.append(list_lab_lab)
        print(list_lab)


    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            if verifyes_x == 1:
                print(verifyes_x)
                return list_lab[0][4], list_lab[0][0]
            else:
                return 0, 0
def Select_last_factor_id():
    verifyes_x = 0
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_IT")
        cursor = connection.cursor()
        sql_select_query = """select * from IT_Factors_lookup order by id DESC limit 1"""
        # set variable in query
        cursor.execute(sql_select_query)
        # fetch result
        record = cursor.fetchall()

        list_lab = []
        for i in range(0, len(record)):
            verifyes_x = 1
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


            list_lab.append(list_lab_lab)
        print(list_lab)


    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            if verifyes_x == 1:
                print(verifyes_x)
                return list_lab[0][0]
            else:
                return 0
def Select_factors_from_server_wordpres(id):
    try:
        connection = mysql.connector.connect(host="185.94.96.98",
                                             user='parso_bazrgani',
                                             password='S{VN^7kOIP7F',
                                             database="parso_tjart")
        cursor = connection.cursor()
        sql_select_query = """select * from pt_wc_orders WHERE id>%s"""
        # set variable in query
        cursor.execute(sql_select_query, (id,))
        # fetch result
        record = cursor.fetchall()
        print(record)
        verifyes_x = 0
        list_lab = []
        for i in range(0, len(record)):
            verifyes_x = 1
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
            if verifyes_x == 1:

                return list_lab
            else:
                return 0
def Insert_new_factors_lookup(data):
    try:
        user_id = ''
        date = datetime.datetime.now()
        cutstomer_name, idssss = Select_name_customer_from_db(data[6])
        print(idssss)
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_IT")
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO IT_Factors_lookup (id, customer_id, seller_id, user_id, type, status, total_price, uploaded, seller_name, customer_name, is_add) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        x = datetime.datetime.now()
        print(x)
        record = (data[0], data[6], 0, user_id, 'IT', 0, 0, date, 'شرکت اصلی', cutstomer_name, 0)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into IT_products table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
def Select_new_factors_details(id):
    try:
        connection = mysql.connector.connect(host="185.94.96.98",
                                             user='parso_bazrgani',
                                             password='S{VN^7kOIP7F',
                                             database="parso_tjart")
        cursor = connection.cursor()
        sql_select_query = """select * from pt_wc_order_product_lookup WHERE order_id=%s"""
        # set variable in query
        cursor.execute(sql_select_query, (id,))
        # fetch result
        record = cursor.fetchall()
        verifyes_x = 0
        list_lab = []

        for i in range(0, len(record)):
            verifyes_x = 1
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

            list_lab.append(list_lab_lab)
        print(list_lab)


    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            if verifyes_x == 1:
                return list_lab
            else:
                return 0
def Insert_new_factors_details(data):
    try:
        for i in data:
            user_id = ''
            date = datetime.datetime.now()
            product_name = Select_name_products_from_db(i[2])
            connection = mysql.connector.connect(host="localhost",
                                                 user='root',
                                                 password='',
                                                 database="ERP_IT")
            cursor = connection.cursor()
            mySql_insert_query = """INSERT INTO IT_Factors_details (id, invoice_id, product_id, count, color, unit, price, total_price, discount_amount, extra_amount, tax, invoice_net, created_at, updated_at, name_products) 
                                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
            x = datetime.datetime.now()
            print(x)
            record = (None, i[1], i[2], i[6], '', 'number', i[8], (i[8]*i[6]), 0,0,0,0, date, date, product_name)
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            print("Record inserted successfully into IT_products table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
def Insert_new_factors_lookup_in_accountig_db(data):
    try:

        user_id = ''
        date = datetime.datetime.now()
        cutstomer_name, idssss = Select_name_customer_from_db(data[6])
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_ACCOUNTING")
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Accounting_Factors_lookup (id, customer_id, seller_id, user_id, type, status, total_price, uploaded, seller_name, customer_name, private_inside_id) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        x = datetime.datetime.now()
        print(x)
        record = (None, idssss, 0, user_id, 'IT', 0, 0, date, 'شرکت اصلی', cutstomer_name, data[0])
        cursor.execute(mySql_insert_query, record)
        pre_invoice_id = cursor.lastrowid
        connection.commit()
        print("Record inserted successfully into IT_products table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return pre_invoice_id
    pass
def Insert_new_factors_details_in_accountig_db(data, invoice_id):
    try:
        for i in data:
            user_id = ''
            date = datetime.datetime.now()
            product_name = Select_name_products_from_db(i[2])
            connection = mysql.connector.connect(host="localhost",
                                                 user='root',
                                                 password='',
                                                 database="ERP_ACCOUNTING")
            cursor = connection.cursor()
            mySql_insert_query = """INSERT INTO Accounting_Factors_details (id, invoice_id, product_id, count, color, unit, price, total_price, discount_amount, extra_amount, tax, invoice_net, created_at, updated_at, name_products) 
                                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
            x = datetime.datetime.now()
            print(x)
            record = (None, invoice_id, i[2], i[6], '', 'number', i[8], (i[8]*i[6]), 0,0,0,0, date, date, product_name)
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            print("Record inserted successfully into IT_products table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
def Start():
    last_factor_id = Select_last_factor_id()
    list_of_new_factors = Select_factors_from_server_wordpres(last_factor_id)
    if list_of_new_factors != 0:
        for i in list_of_new_factors:
            Insert_new_factors_lookup(i)
            list_data_factors_details = Select_new_factors_details(i[0])
            Insert_new_factors_details(list_data_factors_details)
            invoice_id = Insert_new_factors_lookup_in_accountig_db(i)
            Insert_new_factors_details_in_accountig_db(list_data_factors_details, invoice_id)


    else:
        print('we dont have any new factors')
Start()