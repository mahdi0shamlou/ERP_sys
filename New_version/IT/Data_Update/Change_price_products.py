from mysql.connector import connect, Error
import mysql.connector

def Select_data_from_server(id):
    try:
        connection = mysql.connector.connect(host="78.159.108.71",
                                             user='parsot_bazrgani',
                                             password='S{VN^7kOIP7F',
                                             database="parsot_tjart")

        cursor = connection.cursor()
        sql_select_query = """select * from pt_postmeta where (`post_id` = %s)"""
        # set variable in query
        cursor.execute(sql_select_query, (id,))
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
            x = []
            for i in list_lab:
                if i[2] == '_price' or i[2] == '_regular_price':
                    x.append(i)
                    print(i)
            return x
            print("MySQL connection is closed")
def Update_data_for_server(id, price, data):

    try:
        connection = mysql.connector.connect(host="78.159.108.71",
                                             user='parsot_bazrgani',
                                             password='S{VN^7kOIP7F',
                                             database="parsot_tjart")
        for i in data:

            cursor = connection.cursor()
            sql_update_query = """Update pt_postmeta set `meta_value`=%s where `meta_id` = %s"""
            #print(str(data[5]))
            input_data = (price, i[0], )
            cursor.execute(sql_update_query, input_data)
            connection.commit()
            print(f"Record Updated successfully {i[1]} : {price}")

        cursor = connection.cursor()
        sql_update_query = """Update pt_wc_product_meta_lookup set `min_price`=%s, `max_price`=%s where `product_id` = %s"""
        # print(str(data[5]))
        input_data = (price, price, id,)
        cursor.execute(sql_update_query, input_data)
        connection.commit()
        print(f"Record Updated successfully {i[1]} : {price}")

    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



def start(id, price):
    data = Select_data_from_server(id)
    Update_data_for_server(id, price, data)
