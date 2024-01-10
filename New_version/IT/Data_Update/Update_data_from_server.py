from mysql.connector import connect, Error
import mysql.connector
#from ...IT.Products.Get_product_list import Get_product_list
def Get_Update_product_form_server():
    try:
        connection = mysql.connector.connect(host="185.94.96.98",
                                             user='parso_bazrgani',
                                             password='S{VN^7kOIP7F',
                                             database="parso_tjart")
        cursor = connection.cursor()
        sql_select_query = """select * from pt_wc_product_meta_lookup"""
        # set variable in query
        cursor.execute(sql_select_query)
        # fetch result
        record = cursor.fetchall()
        #print(record)
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
            list_lab.append(list_lab_lab)
        #print(list_lab)


    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return list_lab
def Get_product_list():
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_IT")
        cursor = connection.cursor()
        sql_select_query = """select * from IT_test_P"""
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
            list_lab_lab.append(record[i][11])
            list_lab_lab.append(record[i][12])
            list_lab_lab.append(record[i][13])
            list_lab.append(list_lab_lab)
        #print(list_lab)


    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return list_lab
def Find_new_in_products():
    data_server = Get_Update_product_form_server()
    data_local = Get_product_list()
    if len(data_server) != len(data_local):
        # one product added
        Drop_table_products()
        Insert_table_products(data_server)
        pass
    else:
        res = find_change_price(data_server, data_local)
        if res==1:
            Drop_table_products()
            Insert_table_products(data_server)
            pass
        else:
            print('Updated')
        print(len(data_server))
        print(len(data_local))
def find_change_price(data_server, data_local):
    for i in range(0,len(data_server)):
        price_server = data_server[i][4]
        price_local = data_local[i][4]
        if price_server != price_local:
            print(price_local)
            print(price_server)
            print(i)
            return 1
    return 0
def Drop_table_products():
    print('Drop table')
    pass
def Insert_table_products(data_server):
    print('insert table')
    pass
Find_new_in_products()
