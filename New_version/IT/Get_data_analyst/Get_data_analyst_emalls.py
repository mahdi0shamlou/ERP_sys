# Import the requests library
import requests
from bs4 import BeautifulSoup
import mysql.connector
import json
import datetime
#links = ['','',]
str_testy = """https://www.digikala.com/product/dkp-1867422/%D9%BE%D8%B1%DB%8C%D9%86%D8%AA%D8%B1-%D9%84%DB%8C%D8%B2%D8%B1%DB%8C-%D8%A7%DA%86-%D9%BE%DB%8C-%D9%85%D8%AF%D9%84-laserjet-pro-m15w/"""
def Get_torob_data(links):
    str_tst = f'''https://api.torob.com/v4/base-product/sellers/?source=next_desktop&discover_method=direct&_bt__experiment=&search_id=&cities=&province=&prk={links}&list_type=products_info&seed=1705388100'''
    resp = requests.get(str_tst)
    resp = json.loads(resp.text)
    #print(resp['results'][0]['price'])
    avarage = 0
    counter = 0
    for i in resp['results']:
        if i['availability'] == True:

            #print(i['last_price_change_date'])
            if i['last_price_change_date'] != None:
                if 'روز' in i['last_price_change_date'] or 'ماه' in i['last_price_change_date']:
                    #print(i['last_price_change_date'])
                    pass
                else:

                    counter = counter + 1

                    avarage = avarage + i['price']



    if counter > 0:
        avarage = avarage/counter
    else:
        avarage = avarage
    print(avarage)
    avarage = round(avarage, -3)
    numbers = "{:,}".format(avarage)
    #soup = BeautifulSoup(resp.text, "lxml")

    #elements = soup.select('div[class^="seller-element"]')
    #print(resp)
    # print(len(elements))
    #print(numbers)
    return [numbers, avarage]
def Get_dgkala_data(links):
    try:
        str_text = f'https://api.digikala.com/v1/product/{links}/'
        resp = requests.get(str_text)
        resp = json.loads(resp.text)
        #print(resp['data']['product']['default_variant']['price']['selling_price'])
        avarage = round(resp['data']['product']['default_variant']['price']['selling_price'], -3)
        numbers = "{:,}".format(avarage / 10)
        #print(numbers)
        return [numbers, avarage]
    except:
        return ['null', 'null']
def Get_emalls_data(links):
    Emalls_datas = []
# Define the URL of the website to scrape


    # Send a GET request to the specified URL and store the response in 'resp'
    resp = requests.get(links)
    soup = BeautifulSoup(resp.text, "lxml")
    elements = soup.select('div[class^="shop-row"]')
    #print(len(elements))
    price_list = []

    for e in elements:
        #print('########################################################################')
        #print(e)
        #print("Class: ", e["data-price"])
        price_list.append(int(e["data-price"]))
        #print('########################################################################')
    avarage = 0
    for x in price_list:
        avarage = avarage + x

    avarage = avarage / len(price_list)
    avarage = round(avarage,-3)
    numbers = "{:,}".format(avarage/10)

    return [numbers,avarage]
        #print(numbers)
        #print(elements)
        # Print the HTTP status code of the response to check if the request was successful
        #print("Status Code:", resp.status_code)

        # Print the HTML content of the response
        #print("\nResponse Content:")
        #print(resp.text)
def Save_history_price_products(data, price_emalls, price_torob, price_dgkala, avarage_price):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_IT")
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO IT_getdata_price_history (id, product_id, price, date, price_emalls, price_torob, price_dgkala) 
                                 VALUES (%s, %s, %s, %s, %s, %s, %s) """
        x = datetime.datetime.now()
        print(x)
        record = (None, data[0], avarage_price, x, price_emalls, price_torob, price_dgkala)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print(f"Record inserted successfully into IT_getdata_list table ---> {data[1]} AND link is -----> {data[2]}")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
def select_products_from_db():

    try:

        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_IT")
        cursor = connection.cursor()
        sql_select_query = """select * from IT_getdata_list"""
        # set variable in query
        cursor.execute(sql_select_query)
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
            list_lab_lab.append(record[i][4])
            list_lab_lab.append(record[i][5])
            list_lab_lab.append(record[i][6])
            list_lab.append(list_lab_lab)
        #print(list_lab)


    except mysql.connector.Error as error:
        #print("Failed to get record from MySQL table: {}".format(error))
        pass

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            #print("MySQL connection is closed")

            return list_lab
def update_price_into_it_products_price(avarage_price, emalls, torob, dgkala, id):
    try:


        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_IT")

        cursor = connection.cursor()
        sql_update_query = """Update IT_getdata_list set price_emalls = %s, price_torob = %s, price_dgkala = %s, avarage_price=%s where id = %s"""
        # print(str(data[5]))
        input_data = (emalls, torob, dgkala, avarage_price, id,)
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
def start():
    data = select_products_from_db()
    data_finall = []

    for i in data:
        avrage_total = 0
        data_torob = Get_torob_data(i[3])
        data_emalss = Get_emalls_data(i[2])
        data_dgkala = Get_dgkala_data(i[4])

        if data_dgkala[0] == 'null':
            avrage_total = data_torob[1] + (data_emalss[1]/10)
            avrage_total = avrage_total/2
            #print(f'xxxxxx{avrage_total}')
            avrage_total = round(avrage_total, -3)
            numbers = "{:,}".format(avrage_total)
            update_price_into_it_products_price(avrage_total, data_emalss[1]/10, data_torob[1], 000, i[0])
            Save_history_price_products(i, (data_emalss[1]/10), data_torob[1], 0, avrage_total)


        else:
            avrage_total = data_torob[1] + (data_emalss[1]/10) + (data_dgkala[1]/10)
            #print(f'xxxxxx{avrage_total}')
            avrage_total = avrage_total/3
            #print(f'xxxxxx{avrage_total}')
            avrage_total = round(avrage_total, -3)
            #print(f'xxxxxx{avrage_total}')
            numbers = "{:,}".format(avrage_total)
            update_price_into_it_products_price(avrage_total, data_emalss[1]/10, data_torob[1], data_dgkala[1]/10, i[0])
            Save_history_price_products(i, (data_emalss[1] / 10), data_torob[1], data_dgkala[1]/10, avrage_total)

        data_finall.append([i, data_emalss, data_torob, data_dgkala, [numbers, avrage_total]])
    print(data_finall)
    return data_finall
def Get_analysted_data_newst():
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_IT")
        cursor = connection.cursor()
        sql_select_query = """select * from IT_getdata_list"""
        # set variable in query
        cursor.execute(sql_select_query)
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
            list_lab_lab.append(record[i][4])
            list_lab_lab.append(record[i][5])
            list_lab_lab.append(record[i][6])
            list_lab_lab.append("{:,}".format(record[i][7]))
            list_lab_lab.append("{:,}".format(record[i][8]))
            list_lab_lab.append("{:,}".format(record[i][9]))
            list_lab_lab.append("{:,}".format(record[i][10]))
            list_lab.append(list_lab_lab)
        print(list_lab)


    except mysql.connector.Error as error:
        #print("Failed to get record from MySQL table: {}".format(error))
        pass

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            #print("MySQL connection is closed")

            return list_lab


def Get_analysted_data_history(id):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='',
                                             database="ERP_IT")
        cursor = connection.cursor()
        sql_select_query = """select * from IT_getdata_price_history where product_id = %s limit 100"""
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
            list_lab_lab.append(record[i][4])
            list_lab_lab.append(record[i][5])
            list_lab_lab.append(record[i][6])
            list_lab.append(list_lab_lab)
        print(list_lab)


    except mysql.connector.Error as error:
        #print("Failed to get record from MySQL table: {}".format(error))
        pass

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            #print("MySQL connection is closed")

            return list_lab
Get_analysted_data_history(21)
#update_price_into_it_products_price(100,0,0,26)
#Get_dgkala_data('1867422')
#Get_torob_data('d7293468-d1b3-4d86-ace1-7033e1c23996')
#Get_emalls_data('https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_HP-LaserJet-Pro-MFP-M428dw-Multifunction-Printer~id~3581406/')