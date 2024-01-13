from mysql.connector import connect, Error
import mysql.connector
import json
def Get_all_ticket(username):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_USERS")
        cursor = connection.cursor()
        sql_select_query = """select * from Users_ticket where `to` = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (username,))
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
