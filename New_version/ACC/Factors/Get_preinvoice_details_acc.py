from mysql.connector import connect, Error
import mysql.connector

def Get_preinvoice_details_ACC_with_table_lookup(id):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        sql_select_query = """select * from Accounting_PreInvoice_lookup where id = %s"""
        # set variable in query
        cursor.execute(sql_select_query,(id,))
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
def Get_preinvoice_details_ACC_with_table_details(id):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        sql_select_query = """select * from Accounting_PreInvoice_details where invoice_id = %s"""
        # set variable in query
        cursor.execute(sql_select_query,(id,))
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
            list_lab_lab.append("{:,}".format(record[i][6]))
            list_lab_lab.append("{:,}".format(record[i][7]))
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
def Get_preinvoice_customer_details_table_customer_IT(id):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        sql_select_query = """select * from IT_customers where id = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (id,))
        # fetch result
        record = cursor.fetchall()
        list_lab = []
        for i in range(0, len(record)):
            list_lab_lab = []
            list_lab_lab.append(record[i][0])
            list_lab_lab.append(record[i][4])
            list_lab_lab.append(record[i][3])
            list_lab_lab.append(record[i][6])
            list_lab_lab.append(record[i][14])
            list_lab_lab.append(record[i][10])
            list_lab_lab.append(record[i][11])
            list_lab_lab.append(record[i][12])
            list_lab_lab.append(record[i][13])
            list_lab_lab.append(record[i][2])
            list_lab_lab.append(record[i][1])
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
def Get_preinvoice_customer_details_table_customer_SALE(id):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        sql_select_query = """select * from Sale_Coustomer where id = %s"""
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
def Get_preinvoice_seller_details_table_seller_ACC(id):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        sql_select_query = """select * from Accounting_Seller where id = %s"""
        # set variable in query
        cursor.execute(sql_select_query,(id,))
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
def GET_details_preinvoice_acc(id):
    lookup_factors = Get_preinvoice_details_ACC_with_table_lookup(id)
    details_factors = Get_preinvoice_details_ACC_with_table_details(id)
    if lookup_factors[0][4] == "IT":
        customer_data = Get_preinvoice_customer_details_table_customer_IT(lookup_factors[0][1])
    else:
        customer_data = Get_preinvoice_customer_details_table_customer_SALE(lookup_factors[0][1])


    if lookup_factors[0][2] == 0:
        seller_details = [0, 'بارمان سیستم سرزمین پارس', 'تهران خیابان آزادی، خیابان دکتر هوشیار، پلاک ۴۷۴ طبقه دوم واحد 12', '۰۲۱۹۹۹۹۹۹', '۱۰۳۲۰۴۷۱۹۲۵', '۴۱۱۴۶۱۷۶۳۴۷۴', '۳۹۶۴۳۱', '۱۳۴۱۹۶۳۳۳۱']
        seller_details = [0, 'شرکت پرسو تجارت ایرانیان',
                          'تهران هفت تیر کریمخان ایرانشهر پلاک ۲۴۲ طبقه ۵ واحد ۱۰', '02188867100',
                          '10103472930', '411355788865', '10103472930', '1584745337']
    else:
        seller_details = Get_preinvoice_seller_details_table_seller_ACC(lookup_factors[0][2])

    return lookup_factors, details_factors, customer_data, seller_details
