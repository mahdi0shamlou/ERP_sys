from mysql.connector import connect, Error
import mysql.connector

def Send_invoice_to_sended(id):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        sql_update_query = """Update Accounting_Factors_lookup set status = 1 where id = %s"""
        # print(str(data[5]))
        input_data = (id,)
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
def Cancel_preinvoice(id):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        sql_update_query = """Update Accounting_PreInvoice_lookup set status = -1 where id = %s"""
        # print(str(data[5]))
        input_data = (id,)
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
def Send_invoice_to_sended_status_backe(id):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        sql_update_query = """Update Accounting_Factors_lookup set status = 2 where id = %s"""
        # print(str(data[5]))
        input_data = (id,)
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
def Send_invoice_to_sended_status_remove(id):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        sql_update_query = """Update Accounting_Factors_lookup set status = 3 where id = %s"""
        # print(str(data[5]))
        input_data = (id,)
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
def Send_invoice_to_sended_status_okay(id):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        sql_update_query = """Update Accounting_Factors_lookup set status = 4 where id = %s"""
        # print(str(data[5]))
        input_data = (id,)
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
def Send_invoice_to_sended_status_share(id):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")

        cursor = connection.cursor()
        sql_update_query = """Update Accounting_Factors_lookup set status = 1 where id = %s"""
        # print(str(data[5]))
        input_data = (id,)
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

def Invoice_upgrade_status_acc(id):
    try:
        connection = mysql.connector.connect(host="82.115.21.104",
                                             user='barma',
                                             password='ya mahdi',
                                             database="Parso_tejart")
        cursor = connection.cursor()
        sql_select_query = """select * from Accounting_Factors_lookup where id = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (id,))
        # fetch result
        record = cursor.fetchall()
        list_lab = []
        for i in range(0, len(record)):
            list_lab_lab = []
            list_lab_lab.append(record[i][5])
            list_lab.append(list_lab_lab)
        cursor.close()
        cursor = connection.cursor()
        print(list_lab)
        print(list_lab)

        sql_update_query = """Update Accounting_Factors_lookup set status = %s where id = %s"""
        # print(str(data[5]))
        input_data = ((int(list_lab[0][0])+1), id, )
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
Invoice_upgrade_status_acc(727)