from mysql.connector import connect, Error
import mysql.connector
import datetime
def Insert_into_table_products(data, N_id, address):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_IT")
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO IT_customers (id, customer_id, user_id, username, first_name, last_name, email, date_last_active, date_registered, country, postcode, city, state, national_id, address) 
                                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        x = datetime.datetime.now()
        print(x)
        record = (None, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],
        data[11], N_id, address)
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
def Update_data_into_table(data, resault_customer_id):
    for i in range(0, len(data)):
        if str(data[i]) != str(resault_customer_id[0][i + 1]):
            print(data[i])
            print(resault_customer_id[0][i + 1])
            N_id, address = Get_national_code_from_server(data[1])
            try:
                id = resault_customer_id[0][0]

                connection = mysql.connector.connect(host="localhost",
                                                     user='root',
                                                     password='',
                                                     database="ERP_IT")

                cursor = connection.cursor()
                sql_update_query = """Update IT_customers set username = %s, first_name = %s, last_name = %s, email = %s, address=%s, postcode=%s, date_last_active=%s where id = %s"""
                #print(str(data[5]))
                input_data = (data[2],data[3],data[4],data[5],address,data[9],data[6],id)
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
def Get_national_code_from_server(C_id):
    try:
        connection = mysql.connector.connect(host="185.94.96.98",
                                             user='parso_bazrgani',
                                             password='S{VN^7kOIP7F',
                                             database="parso_tjart")
        cursor = connection.cursor()
        sql_select_query = """select * from pt_usermeta WHERE user_id = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (C_id,))
        # fetch result
        record = cursor.fetchall()
        # print(record)
        list_lab = []
        for i in range(0, len(record)):
            list_lab_lab = []
            list_lab_lab.append(record[i][0])
            list_lab_lab.append(record[i][1])
            list_lab_lab.append(record[i][2])
            list_lab_lab.append(record[i][3])

            list_lab.append(list_lab_lab)
        #print(list_lab)


    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            n_id = ''
            address = ''
            for i in list_lab:
                if i[2] == 'mellicode_1703934173824':
                    n_id = i[3]
                if i[2] == 'billing_address_1':
                    address = i[3]
            return n_id, address
def Select_Customer(id):
    verifyes_x = 0
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_IT")
        cursor = connection.cursor()
        sql_select_query = """select * from IT_customers where customer_id = %s"""
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
def Insert_update_new_in_DB(data):
    resault_customer_id = Select_Customer(data[0])
    if resault_customer_id == 0:
        N_id, address = Get_national_code_from_server(data[1])
        Insert_into_table_products(data, N_id, address)
        '''insert'''
        return 1
    else:

        Update_data_into_table(data, resault_customer_id)

        '''update'''
        return 1
def Get_Update_customer_form_server():
    try:
        connection = mysql.connector.connect(host="185.94.96.98",
                                             user='parso_bazrgani',
                                             password='S{VN^7kOIP7F',
                                             database="parso_tjart")
        cursor = connection.cursor()
        sql_select_query = """select * from pt_wc_customer_lookup"""
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
    resault = Get_Update_customer_form_server()
    for i in resault:
        #print(i)
        resault_DB = Insert_update_new_in_DB(i)
#Start()
