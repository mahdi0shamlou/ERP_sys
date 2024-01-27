from mysql.connector import connect, Error
import mysql.connector
import datetime
def Select_products(id):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_IT")
        cursor = connection.cursor()
        sql_select_query = """select * from IT_products where product_id = %s"""
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
            list_lab_lab.append(record[i][13])
            list_lab_lab.append(record[i][14])
            list_lab.append(list_lab_lab)
        #print(list_lab)


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
    pass
def Insert_into_table_products(data):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_IT")
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO IT_products (id, product_id, sku, virtuals, downloadable, min_price, max_price, onsale, stock_quantity, stock_status, rating_count, average_rating, total_sales, tax_status, tax_class) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        x = datetime.datetime.now()
        print(x)
        record = (None, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13])
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
def Update_data_into_table(data, resault_product_id):
    for i in range(0, len(data)):
        if data[i] != resault_product_id[0][i+1]:
            try:
                id = resault_product_id[0][0]
                min_price = data[4]
                max_price = data[5]
                connection = mysql.connector.connect(host="localhost",
                                                     user='root',
                                                     password='',
                                                     database="ERP_IT")

                cursor = connection.cursor()
                sql_update_query = """Update IT_products set min_price = %s, max_price = %s where id = %s"""
                input_data = (min_price, max_price, id)
                cursor.execute(sql_update_query, input_data)
                connection.commit()
                print(f"Record Updated successfully {id}")

            except mysql.connector.Error as error:
                print("Failed to update record to database: {}".format(error))
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")

            pass
        else:
            pass
def Insert_update_new_in_DB(data):
    resault_product_id = Select_products(data[0])
    if resault_product_id == 0:
        Insert_into_table_products(data)

        '''insert'''
        return 1
    else:
        Update_data_into_table(data, resault_product_id)

        '''update'''
        return 1
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
def Start():
    resault = Get_Update_product_form_server()
    for i in resault:
        resault_DB = Insert_update_new_in_DB(i)


#Start()