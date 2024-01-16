from flask import Flask, render_template, redirect, request, session, json
from flask_session.__init__ import Session
from Login.main import Check_login #this method do work for login section
from Login.logout import insert_log_login_logout #this method do work for login section
from IT.Products.Get_product_list import Get_product_list, Get_product_details #this method get product from local database
from IT.Customer.Get_site_customer import Get_site_customer_list
from IT.Data_Update.Update_products_value import Start as Start_get_Update_Products_from_server
from IT.Data_Update.Update_customer_value import Start as Start_get_Update_Customers_from_server
from IT.Ticket.Get_all_ticket import Get_all_ticket
from IT.Customer.Get_G_customer import Get_g_customer_list, Get_g_customer_details
from IT.Customer.Add_customer import Insert_g_cutomer
from IT.Pre_invoice.Add_preinvoice import Add_preinvoice_IT
from IT.Pre_invoice.Get_preinvoice import Get_IT_preinvoice_details, Get_IT_preinvoice_lookup
from IT.Pre_invoice.Delet_preinvoice import delet_preinvoice_it
from IT.Get_data_analyst.Get_data_analyst_emalls import start as Data_collection_section
from IT.Get_data_analyst.Insert_links import insert_links_to_db_getdata
from IT.Get_data_analyst.delet_links import delet_link_data_from_db
from ACC.Get_PreInvoice_lookup import Get_PreInvoice_lookup_list
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
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404/index.html'), 404

@app.errorhandler(504)
def internal_error(error):
    return render_template('504/index.html'), 504
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

#---------------------------------------------------------------------------------------------------
#---------------------------------------------- START IT SECTION
#---------------------------------------------------------------------------------------------------
@app.route("/IT")
def IT():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        path = session.get('Path')
        tickets = Get_all_ticket(session.get("Username"))
        return render_template("/IT/index.html", tickets=tickets, user=session.get('Username'), pathmain=path, email=session.get('email'))
@app.route('/IT/Pre_Invoice')
def Pre_invoice():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        path = session.get('Path')
        pre_invoice_list = Get_PreInvoice_lookup_list()
        return render_template("/IT/Pre_invoice/index.html", pre_invoice_list=pre_invoice_list, user=session.get('Username'), pathmain=path, email=session.get('email'))
@app.route('/IT/Pre_invoice_add')
def Pre_Invoice_add():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        path = session.get('Path')
        list_costumers = Get_g_customer_list()
        return render_template("/IT/Pre_invoice/Pre_Invoice_add_customer.html", list_costumers=list_costumers, user=session.get('Username'), pathmain=path, email=session.get('email'))
@app.route('/IT/Pre_invoice_add_products')
def Pre_invoice_add_products():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        ID_C = request.args.get('ID_C')
        path = session.get('Path')
        list_costumers = Get_g_customer_details(ID_C)
        list_product = Get_product_list()
        return render_template("/IT/Pre_invoice/Pre_invoice_add_products.html", ID_C=ID_C, list_product=list_product, list_costumers=list_costumers, user=session.get('Username'), pathmain=path, email=session.get('email'))
#_______________________________---dar dast eghdam
@app.route('/IT/add_preinvoice_finall')
def Add_preinvoice_finall():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        ID_C = request.args.get('ID_C')
        NAME_C = request.args.get('NAME_C')
        products = request.args.getlist('product[]', type=str)
        products_number = request.args.getlist('product_number[]', type=str)
        product_name_p = request.args.getlist('product_name_p[]', type=str)
        product_number_p = request.args.getlist('product_number_p[]', type=str)
        product_price_p = request.args.getlist('product_price_p[]', type=str)
        Add_preinvoice_IT(ID_C, products, products_number, product_name_p, product_number_p, product_price_p, session.get("Username"), NAME_C)
        path = session.get('Path')
        return redirect('/IT/Pre_Invoice')
#_______________________________---dar dast eghdam

@app.route("/IT/Product_list")
def IT_Product_list():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        path = session.get('Path')
        Product_list = Get_product_list()
        return render_template("/IT/Product_list/index.html", user=session.get('Username'), pathmain=path, email=session.get('email'), Product_list=Product_list)
@app.route("/IT/Customers")
def IT_Customers():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        path = session.get('Path')
        Customer_list = Get_site_customer_list()
        return render_template("/IT/Customer/index.html", Customer_list=Customer_list, user=session.get('Username'), pathmain=path, email=session.get('email'))
@app.route("/IT/Customers_G")
def IT_Customers_G():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        path = session.get('Path')
        Customer_list = Get_g_customer_list()
        return render_template("/IT/Customer/index_G.html", Customer_list=Customer_list, user=session.get('Username'), pathmain=path, email=session.get('email'))
@app.route("/IT/ADD_Customers_G")
def IT_ADD_Customers_G():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        path = session.get('Path')
        return render_template("/IT/Customer/Add_customer_G.html", user=session.get('Username'), pathmain=path, email=session.get('email'))
@app.route("/IT/Insert_Customers_G", methods=["POST", "GET"])
def IT_Insert_Customers_G():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        N_id = request.args.get('N_id')
        address = request.args.get('address')
        data = []
        data.append(0)
        data.append(0)
        data.append(request.args.get('username'))
        data.append(request.args.get('firstname'))
        data.append(request.args.get('lastname'))
        data.append(request.args.get('email'))
        data.append(request.args.get('city'))
        data.append(request.args.get('postcode'))
        Insert_g_cutomer(data, N_id, address)
        #path = session.get('Path')
        return redirect('/')

@app.route("/IT/Update_all_data_online_from_server")
def IT_Update_data():
    print('x')
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        if session.get("Username") == 'hoseinraz' or session.get("Username") == 'admin':
            Start_get_Update_Products_from_server()
            Start_get_Update_Customers_from_server()
            return redirect('/')
        else:
            return 'you have not premision'



@app.route("/IT/Pre_invoice_details_it", methods=["POST", "GET"])
def Pre_invoice_details_it():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        pre_invoice_id = request.args.get('P_ID')
        pre_invoice_data = Get_IT_preinvoice_details(pre_invoice_id)
        pre_invoice_lookup = Get_IT_preinvoice_lookup(pre_invoice_id)
        customer_id = pre_invoice_lookup[0][1]
        customer_details = Get_g_customer_details(customer_id)

        total_price = 0
        for i in pre_invoice_data:
            total_price = total_price + int(i[7])
        path = session.get('Path')
        return render_template('/IT/Pre_invoice/Pre_invoice_details.html',pre_invoice_lookup=pre_invoice_lookup, customer_details=customer_details, total_price=total_price , len_code=len(pre_invoice_data), pre_invoice_data=pre_invoice_data, user=session.get('Username'), pathmain=path, email=session.get('email'))
@app.route("/IT/preinvoice_delet_it", methods=["POST", "GET"])
def preinvoice_delet_it():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        pre_invoice_id = request.args.get('id')
        delet_preinvoice_it(pre_invoice_id)
        return redirect('/IT/Pre_Invoice')


@app.route("/IT/preinvoice_print_it", methods=["POST", "GET"])
def preinvoice_print_it():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        pre_invoice_id = request.args.get('id')
        pre_invoice_data = Get_IT_preinvoice_details(pre_invoice_id)
        pre_invoice_lookup = Get_IT_preinvoice_lookup(pre_invoice_id)
        customer_id = pre_invoice_lookup[0][1]
        customer_details = Get_g_customer_details(customer_id)

        total_price = 0
        for i in pre_invoice_data:
            total_price = total_price + int(i[7])
        path = session.get('Path')
        return render_template('/IT/Pre_invoice/Pre_invoice_print.html',pre_invoice_lookup=pre_invoice_lookup, customer_details=customer_details, total_price=total_price , len_code=len(pre_invoice_data), pre_invoice_data=pre_invoice_data, user=session.get('Username'), pathmain=path, email=session.get('email'))


@app.route('/IT/add_linksgetdata', methods=["POST", "GET"])
def add_linksgetdata():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        name = request.args.get('name')
        link = request.args.get('link')
        link_torob = request.args.get('link_torob')
        link_dg = request.args.get('link_dg')
        site = '0'
        insert_links_to_db_getdata(link, name, site, link_torob, link_dg)
        return redirect('/IT/getdata')
@app.route('/IT/delet_linksgetdata', methods=["POST", "GET"])
def delet_linksgetdata():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        id = request.args.get('id')
        delet_link_data_from_db(id)
        return redirect('/IT/getdata')
@app.route('/IT/getdata')
def getdata():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        path = session.get('Path')
        main_data = Data_collection_section()
        print(main_data)
        return render_template('/IT/Get_data/index.html', main_data=main_data, user=session.get('Username'), pathmain=path, email=session.get('email'))
@app.route("/IT/print_getdata_sction", methods=["POST", "GET"])
def print_getdata_sction():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        path = session.get('Path')
        main_data = Data_collection_section()
        print(main_data)
        return render_template('/IT/Get_data/print.html', main_data=main_data, user=session.get('Username'), pathmain=path, email=session.get('email'))
#---------------------------------------------------------------------------------------------------
#---------------------------------------------- END IT SECTION
#---------------------------------------------------------------------------------------------------





if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=1000)

