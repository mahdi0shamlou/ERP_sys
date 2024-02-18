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
def Send_preinvoice_to_invoice(id):
    lookup_data = Get_preinvoice_details_ACC_with_table_lookup(id)
    details_data = Get_preinvoice_details_ACC_with_table_details(id)
    try:
        if lookup_data[0][5] != 1:
            connection = mysql.connector.connect(host="82.115.21.104",
                                                 user='barma',
                                                 password='ya mahdi',
                                                 database="Parso_tejart")

            cursor = connection.cursor()
            sql_update_query = """Update Accounting_PreInvoice_lookup set status = 1 where id = %s"""
            # print(str(data[5]))
            input_data = (id,)
            cursor.execute(sql_update_query, input_data)
            connection.commit()
            print(f"Record Updated successfully {id}")


            mySql_insert_query = """INSERT INTO Accounting_Factors_lookup (id, customer_id, seller_id, user_id, type, status, total_price, uploaded, seller_name, customer_name, private_inside_id) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

            print(lookup_data)
            record = (None, lookup_data[0][1], lookup_data[0][2], lookup_data[0][3], lookup_data[0][4], 0, lookup_data[0][6], lookup_data[0][7], lookup_data[0][8], lookup_data[0][9], 0)
            cursor.execute(mySql_insert_query, record)
            pre_invoice_id = cursor.lastrowid
            connection.commit()
            print("Record inserted successfully into IT_products table")

            for i in details_data:
                mySql_insert_query = """INSERT INTO Accounting_Factors_details (id, invoice_id, product_id, count, color, unit, price, total_price, discount_amount, extra_amount, tax, invoice_net, created_at, updated_at, name_products) 
                                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

                record = (None, pre_invoice_id, i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10],i[11], i[12], i[13], i[14])
                cursor.execute(mySql_insert_query, record)
                connection.commit()
                print("Record inserted successfully into IT_products table")
            sql_update_query = """Update Accounting_PreInvoice_lookup set status = 1 where id = %s"""
            # print(str(data[5]))
            input_data = (id,)
            cursor.execute(sql_update_query, input_data)
            connection.commit()
            print(f"Record Updated successfully {id}")
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
