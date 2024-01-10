from flask import Flask, render_template, redirect, request, session, json
from flask_session import Session
from Login.main import Check_login
from Login.logout import insert_log_login_logout
from IT.it_main import Get_Logs
from SA.sa_main import Get_preinvoice
from SA.sa_preinvoice_details import Get_preinvoice_details
from SA.sa_preinvoice_delet import Preinvoice_delet
from SA.sa_getcustomer import Get_all_sale_customer_details
from SA.sa_preinvoice_details import Get_sale_customer_details
from SA.SA_product import Get_product_details, Get_all_product_details
from SA.sa_insert_preinvoice import insert_preinvoice




app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def Home():
    if not session.get("Username"):
        return redirect("/Login")
    path = session.get('Path')
    return redirect(f"/{path}")

#---------------------------------------------------------------------------------------------------
#---------------------------------------------- START LOGIN SECTION
#---------------------------------------------------------------------------------------------------
@app.route("/Login", methods=["POST", "GET"])
def Login():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        path = session.get('Path')
        return redirect(f"/{path}")

@app.route("/Login_check", methods=["POST", "GET"])
def Login_check():
    if request.args.get("username") is None or request.args.get("pass") is None:
        return redirect("/Login")
    else:
        user = request.args.get("username")
        password = request.args.get("pass")
        Check_login_resualt = Check_login(user, password)
        return Check_login_resualt


@app.route("/logout")
def logout():
    insert_log_login_logout(None,'2023', session["Username"], 'logout')
    session["Username"] = None
    session["Access_level"] = None
    return redirect("/")

#---------------------------------------------------------------------------------------------------
#---------------------------------------------- END LOGIN SECTION
#---------------------------------------------------------------------------------------------------
@app.route("/IT")
def IT():
    path = session.get('Path')
    auth = session.get('Access_level')
    if auth==0 or auth == 5:
        record_logs = Get_Logs(5)
        return render_template('IT/index.html',user=session.get('Username'), pathmain=path, email=session.get('email'), record_logs=record_logs)
    else:
        return 'You have not premision'

@app.route("/ACC")
def ACC():
    path = session.get('Path')
    auth = session.get('Access_level')
    if auth==4 or auth == 5:
        record_logs = Get_Logs(5)
        list_preinvoice = Get_preinvoice(0)
        return render_template('ACC/index.html',user=session.get('Username'), pathmain=path, email=session.get('email'), record_logs=record_logs, preinvoice=list_preinvoice)
    else:
        return 'You have not premision'

@app.route("/ACC/list_product")
def list_product():
    path = session.get('Path')
    auth = session.get('Access_level')
    if auth==4 or auth == 5:
        record_logs = Get_Logs(5)
        list_preinvoice = Get_preinvoice(0)
        return render_template('ACC/list_product.html',user=session.get('Username'), pathmain=path, email=session.get('email'), record_logs=record_logs, preinvoice=list_preinvoice)
    else:
        return 'You have not premision'
@app.route("/MA")
def MA():
    path = session.get('Path')
    auth = session.get('Access_level')
    if auth==2 or auth == 5:
        return 'Hello This is page of managment'
    else:
        return 'You have not premision'
#---------------------------------------------------------------------------------------------------
#---------------------------------------------- START SALE SECTION
#---------------------------------------------------------------------------------------------------
@app.route("/SA")
def SA():
    path = session.get('Path')
    auth = session.get('Access_level')
    if auth==4 or auth == 5:
        record_logs = Get_Logs(5)
        list_preinvoice = Get_preinvoice(0)
        return render_template('SA/index.html',user=session.get('Username'), pathmain=path, email=session.get('email'), record_logs=record_logs, preinvoice=list_preinvoice)
    else:
        return 'You have not premision'



#---------------------------------------------------------------------------------------------------
#---------------------------------------------- Start PRE INVOICE
#---------------------------------------------------------------------------------------------------
@app.route("/SA/preinvoice")
def preinvoice_sa():
    path = session.get('Path')
    auth = session.get('Access_level')
    if auth==4 or auth == 5:
        record_logs = Get_Logs(5)
        list_preinvoice = Get_preinvoice(0)
        return render_template('SA/Pre_invoice/preinvoice.html',user=session.get('Username'), pathmain=path, email=session.get('email'), record_logs=record_logs, preinvoice=list_preinvoice)
    else:
        return 'You have not premision'
@app.route("/SA/preinvoice_add")
def preinvoice_add_sa():
    customer_id = request.args.get('id_customer')
    private_id_num = request.args.get('private_id_num')
    products = request.args.getlist('product[]', type=str)
    path = session.get('Path')
    auth = session.get('Access_level')
    if auth==4 or auth == 5:
        #record_logs = Get_Logs(5)
        list_costumers = Get_all_sale_customer_details(0)
        return render_template('SA/Pre_invoice/preinvice_add_customer.html',user=session.get('Username'), pathmain=path, email=session.get('email'), list_costumers=list_costumers)
    else:
        return 'You have not premision'
@app.route("/SA/add_preinvoice_products", methods=["POST", "GET"])
def add_preinvoice_products():
    customer_id = request.args.get('customer')
    private_id_num = request.args.get('private_id_num')
    products = request.args.getlist('product[]', type=str)
    path = session.get('Path')
    auth = session.get('Access_level')
    if auth==4 or auth == 5:
        #record_logs = Get_Logs(5)
        list_costumers = Get_sale_customer_details(customer_id)
        list_product = Get_all_product_details()
        return render_template('SA/Pre_invoice/add_preinvoice_products.html',list_product=list_product, private_id_num = private_id_num, user=session.get('Username'), pathmain=path, email=session.get('email'), list_costumers=list_costumers)
    else:
        return 'You have not premision'

@app.route("/SA/add_preinvoice_finall", methods=["POST", "GET"])
def add_preinvoice_finall():
    customer_id = request.args.get('customer')
    private_id_num = request.args.get('private_id_num')
    products = request.args.getlist('product[]', type=str)
    products_number = request.args.getlist('product_number[]', type=str)
    path = session.get('Path')
    auth = session.get('Access_level')
    if auth == 4 or auth == 5:
        # record_logs = Get_Logs(5)
        list_costumers = Get_sale_customer_details(customer_id)
        list_products = Get_product_details(products, products_number)

        return render_template('SA/Pre_invoice/add_preinvoice_finall.html', private_id_num=private_id_num,
                               user=session.get('Username'), pathmain=path, email=session.get('email'),
                               list_costumers=list_costumers, list_products=list_products)
    else:
        return 'You have not premision'
@app.route("/SA/add_preinvoice_finall_insert", methods=["POST", "GET"])
def add_preinvoice_finall_insert():
    customer_id = request.args.get('customer')
    private_id_num = request.args.get('private_id_num')
    products = request.args.getlist('product[]', type=str)
    products_number = request.args.getlist('product_number[]', type=str)


    path = session.get('Path')
    auth = session.get('Access_level')
    if auth == 4 or auth == 5:
        # record_logs = Get_Logs(5)
        list_costumers = Get_sale_customer_details(customer_id)
        list_products = Get_product_details(products, products_number)
        usenamr = session.get('Username')
        p = insert_preinvoice('', private_id_num, list_products, customer_id, usenamr, path)
        return redirect('/SA/preinvoice')
    else:
        return 'You have not premision'
@app.route("/SA/pre_invoice_detilas", methods=["POST", "GET"])
def pre_invoice_detilas():
    path = session.get('Path')
    auth = session.get('Access_level')
    if auth==4 or auth == 5:
        ids = request.args.get('id')
        #record_logs = Get_Logs(5)
        list_preinvoice = Get_preinvoice_details(ids)

        return render_template('SA/Pre_invoice/preinvoice_details.html',user=session.get('Username'), pathmain=path, email=session.get('email'), details=list_preinvoice[0], lens_codes=len(list_preinvoice[0][2]))
    else:
        return 'You have not premision'

@app.route("/SA/preinvoice_print", methods=["POST", "GET"])
def pre_invoice_print():
    path = session.get('Path')
    auth = session.get('Access_level')
    if auth==4 or auth == 5:
        ids = request.args.get('id')
        #record_logs = Get_Logs(5)
        list_preinvoice = Get_preinvoice_details(ids)

        return render_template('SA/Pre_invoice/pre_invoice_print.html',user=session.get('Username'), pathmain=path, email=session.get('email'), details=list_preinvoice[0], lens_codes=len(list_preinvoice[0][2]), addres_mohr=session.get('mohr_address'))
    else:
        return 'You have not premision'
@app.route("/SA/Pre_invoice/preinvoice_delet", methods=["POST", "GET"])
def preinvoice_delet():
    path = session.get('Path')
    auth = session.get('Access_level')
    if auth==4 or auth == 5:
        ids = request.args.get('id')
        #record_logs = Get_Logs(5)
        Preinvoice_delet(ids)
        #list_preinvoice = Get_preinvoice_details(ids)

        return render_template('SA/preinvoice_delet.html')
    else:
        return 'You have not premision'

#---------------------------------------------------------------------------------------------------
#---------------------------------------------- END PRE INVOICE
#---------------------------------------------------------------------------------------------------







@app.route("/SA/list_costumer")
def list_costumer():
    path = session.get('Path')
    auth = session.get('Access_level')
    if auth==4 or auth == 5:
        record_logs = Get_Logs(5)
        list_preinvoice = Get_preinvoice(0)
        return render_template('SA/list_costumer.html',user=session.get('Username'), pathmain=path, email=session.get('email'), record_logs=record_logs, preinvoice=list_preinvoice)
    else:
        return 'You have not premision'
@app.route("/SA/list_costumer_vip")
def list_costumer_vip():
    path = session.get('Path')
    auth = session.get('Access_level')
    if auth==4 or auth == 5:
        record_logs = Get_Logs(5)
        list_preinvoice = Get_preinvoice(0)
        return render_template('SA/list_costumer_vip.html',user=session.get('Username'), pathmain=path, email=session.get('email'), record_logs=record_logs, preinvoice=list_preinvoice)
    else:
        return 'You have not premision'
@app.route("/SA/invoice")
def invoice_sa():
    path = session.get('Path')
    auth = session.get('Access_level')
    if auth==4 or auth == 5:
        record_logs = Get_Logs(5)
        list_preinvoice = Get_preinvoice(0)
        return render_template('SA/invoice.html',user=session.get('Username'), pathmain=path, email=session.get('email'), record_logs=record_logs, preinvoice=list_preinvoice)
    else:
        return 'You have not premision'



@app.route("/SA/get_info_customer", methods=["POST", "GET"])
def get_info_customer():


        ids = request.args.get('id')
        datas = Get_sale_customer_details(ids)
        print(datas[0])
        data = {}
        for i in datas:
            data = {"id" : i[0], "name" : i[1], "address" : i[4], "national_id" : i[3], "phone" : i[8]}

        return json.dumps(data)


@app.route("/CO")
def CO():
    auth = session.get('Access_level')
    if auth==3 or auth == 5:
        return 'Hello This is page of Commerce'
    else:
        return 'You have not premision'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)



'''
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        create_db_query = "CREATE DATABASE ERP_AC"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)

'''
'''
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="online_movie_rating",
    ) as connection:
        print(connection)
except Error as e:
    print(e)
'''