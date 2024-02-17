from flask import Flask, render_template, redirect, request, session, json
from datetime import timedelta
from flask_session.__init__ import Session
from Login.main import Check_login #this method do work for login section
from Login.logout import insert_log_login_logout #this method do work for login section
from IT.Products.Get_product_list import Get_product_list, Get_product_details #this method get product from local database
from IT.Customer.Get_site_customer import Get_site_customer_list
from IT.Data_Update.Update_products_value import Start as Start_get_Update_Products_from_server
from IT.Data_Update.Update_customer_value import Start as Start_get_Update_Customers_from_server
from IT.Data_Update.Update_factors_value import Start as Start_get_Update_Factors_from_server
from IT.Ticket.Get_all_ticket import Get_all_ticket_new, Get_ticket_details, Get_all_ticket_list
from IT.Ticket.Add_ticket import start as insert_ticket_at_start_ticket
from IT.Ticket.Add_ticket import Add_message_IT, Add_status_IT
from IT.Customer.Get_G_customer import Get_g_customer_list, Get_g_customer_details, Get_customer_details_it_with_userid
from IT.Customer.Add_customer import Insert_g_cutomer
from IT.Pre_invoice.Add_preinvoice import Add_preinvoice_IT
from IT.Pre_invoice.Get_preinvoice import Get_IT_preinvoice_details, Get_IT_preinvoice_lookup
from IT.Pre_invoice.Delet_preinvoice import delet_preinvoice_it
from IT.Get_data_analyst.Get_data_analyst_emalls import start as Data_collection_section
from IT.Get_data_analyst.Get_data_analyst_emalls import Get_analysted_data_newst, Get_analysted_data_history
from IT.Get_data_analyst.Insert_links import insert_links_to_db_getdata
from IT.Get_data_analyst.delet_links import delet_link_data_from_db
from ACC.Get_PreInvoice_lookup import Get_PreInvoice_lookup_list
from IT.Factors.Get_factors_lookup_IT import Get_factors_lookup_IT, Get_factors_lookup_IT_with_limits
from IT.Factors.Get_factors_detials_IT import Get_IT_Factors_lookup, Get_IT_Factors_details
from ACC.Factors.Get_factors_look_up import Get_factors_lookup_ACC_with_limits, Get_factors_lookup_ACC_with_pages, Get_factors_sended_lookup_ACC_with_pages
from ACC.Factors.Get_factors_details_acc import GET_details_factors_acc
from ACC.Factors.Get_preinvoice_details_acc import GET_details_preinvoice_acc
from ACC.Factors.Get_preinvoice_look_up import Get_preinvoice_lookup_ACC_with_limits, Get_preinvoice_lookup_ACC_with_pages
from ACC.Factors.Send_invoice_sended_section import Send_invoice_to_sended, Send_invoice_to_sended_status_remove, Send_invoice_to_sended_status_backe, Send_invoice_to_sended_status_okay
from ACC.Factors.Send_preinvoice_to_invoice import Send_preinvoice_to_invoice
from ACC.Factors.Get_Factors_from_DB import Get_factors_lookup_IT_sended_section_fro_pages, Get_factors_lookup_IT_only_factors_fro_pages
from IT.Data_Update.Change_price_products import start as Change_products_price_to_seve
from SA.Customer.Get_customer import Get_customer_list_SA, Get_customer_list_SA_add_preinvoice, Get_customer_details
from SA.Customer.Add_customer_SA import Insert_cutomer_SA
from SA.Customer.Delet_customer_SA import Delet_Customer_SA
from SA.Pre_invoice.Get_Preinvoice import Get_preinvoice_lookup_SA_with_pages
from SA.Pre_invoice.Get_products import Get_products_list_SA_add_preinvoice, Get_product_add_preinvoice
from SA.Pre_invoice.Insert_preinvoice_sa import Add_preinvoice_SA
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=15)
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
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            path = session.get('Path')
            tickets = Get_all_ticket_new(path)
            list_factors = Get_factors_lookup_IT_with_limits()
            return render_template("/IT/index.html", list_factors=list_factors, tickets=tickets, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route('/IT/Pre_Invoice')
def Pre_invoice():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            path = session.get('Path')
            pre_invoice_list = Get_preinvoice_lookup_ACC_with_pages(10000)
            return render_template("/IT/Pre_invoice/index.html", pre_invoice_list=pre_invoice_list, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route('/IT/Invoice_sended')
def Invoice_sended_IT_section():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            path = session.get('Path')
            sended_invoice_it = Get_factors_lookup_IT_sended_section_fro_pages(10000)
            return render_template("/IT/Invoice/Invoice_sended.html", pre_invoice_list=sended_invoice_it, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route('/IT/Pre_invoice_add')
def Pre_Invoice_add():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            path = session.get('Path')
            list_costumers = Get_g_customer_list()
            return render_template("/IT/Pre_invoice/Pre_Invoice_add_customer.html", list_costumers=list_costumers, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route('/IT/Pre_invoice_add_products')
def Pre_invoice_add_products():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            ID_C = request.args.get('ID_C')
            path = session.get('Path')
            list_costumers = Get_g_customer_details(ID_C)
            list_product = Get_product_list()
            return render_template("/IT/Pre_invoice/Pre_invoice_add_products.html", ID_C=ID_C, list_product=list_product, list_costumers=list_costumers, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route('/IT/add_preinvoice_finall')
def Add_preinvoice_finall():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
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
        else:
            return render_template('Not_Permission/index.html')
@app.route("/IT/Product_list")
def IT_Product_list():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            path = session.get('Path')
            Product_list = Get_product_list()
            return render_template("/IT/Product_list/index.html", user=session.get('Username'), pathmain=path, email=session.get('email'), Product_list=Product_list)
        else:
            return render_template('Not_Permission/index.html')
@app.route("/IT/Customers")
def IT_Customers():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            path = session.get('Path')
            Customer_list = Get_site_customer_list()
            return render_template("/IT/Customer/index.html", Customer_list=Customer_list, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/IT/Customers_G")
def IT_Customers_G():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            path = session.get('Path')
            Customer_list = Get_g_customer_list()
            return render_template("/IT/Customer/index_G.html", Customer_list=Customer_list, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/IT/ADD_Customers_G")
def IT_ADD_Customers_G():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            path = session.get('Path')
            return render_template("/IT/Customer/Add_customer_G.html", user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/IT/Insert_Customers_G", methods=["POST", "GET"])
def IT_Insert_Customers_G():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
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
        else:
            return render_template('Not_Permission/index.html')

@app.route("/IT/Update_all_data_online_from_server")
def IT_Update_data():
    print('x')
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            if session.get("Username") == 'hoseinraz' or session.get("Username") == 'admin':
                Start_get_Update_Products_from_server()
                Start_get_Update_Customers_from_server()
                Start_get_Update_Factors_from_server()
                return redirect('/')
            else:
                return 'you have not premision'
        else:
            return render_template('Not_Permission/index.html')
@app.route("/IT/Pre_invoice_details_it", methods=["POST", "GET"])
def Pre_invoice_details_it():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
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
        else:
            return render_template('Not_Permission/index.html')
@app.route("/IT/preinvoice_delet_it", methods=["POST", "GET"])
def preinvoice_delet_it():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            pre_invoice_id = request.args.get('id')
            delet_preinvoice_it(pre_invoice_id)
            return redirect('/IT/Pre_Invoice')
        else:
            return render_template('Not_Permission/index.html')
@app.route("/IT/preinvoice_print_it", methods=["POST", "GET"])
def preinvoice_print_it():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            pre_invoice_id = request.args.get('id')
            lookup_factors, details_factors, customer_data, seller_details = GET_details_preinvoice_acc(pre_invoice_id)
            invoice_total_price = 0
            for i in details_factors:
                invoice_total_price = invoice_total_price + i[7]

            invoice_total_price = "{:,}".format(invoice_total_price)
            print(seller_details)

            return render_template('/IT/Pre_invoice/Pre_invoice_print.html', invoice_total_price=invoice_total_price, lookup_factors=lookup_factors, details_factors=details_factors, customer_data=customer_data, seller_details=seller_details)
        else:
            return render_template('Not_Permission/index.html')
@app.route('/IT/add_linksgetdata', methods=["POST", "GET"])
def add_linksgetdata():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            name = request.args.get('name')
            link = request.args.get('link')
            link_torob = request.args.get('link_torob')
            link_dg = request.args.get('link_dg')
            site = '0'
            insert_links_to_db_getdata(link, name, site, link_torob, link_dg)
            return redirect('/IT/getdata')
        else:
            return render_template('Not_Permission/index.html')
@app.route('/IT/delet_linksgetdata', methods=["POST", "GET"])
def delet_linksgetdata():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            id = request.args.get('id')
            delet_link_data_from_db(id)
            return redirect('/IT/getdata')
        else:
            return render_template('Not_Permission/index.html')

@app.route('/IT/getdata_update')
def update_getdata():
    try:
        if not session.get("Username"):
            return render_template("/Login/Login_v4/index.html")
        else:
            auth = session.get('Access_level')
            if auth == 0 or auth == 5:
                path = session.get('Path')
                main_data = Data_collection_section()
                print(main_data)
                return redirect('/IT/getdata')
            else:
                return render_template('Not_Permission/index.html')
    except:
        return render_template('Error/index.html')
@app.route('/IT/getdata')
def getdata():
    try:

        if not session.get("Username"):
            return render_template("/Login/Login_v4/index.html")
        else:
            auth = session.get('Access_level')
            if auth == 0 or auth == 5:
                path = session.get('Path')
                main_data = Get_analysted_data_newst()
                print(main_data)
                return render_template('/IT/Get_data/index.html', main_data=main_data, user=session.get('Username'), pathmain=path, email=session.get('email'))
            else:
                return render_template('Not_Permission/index.html')
    except:
        return render_template('Error/index.html')
@app.route("/IT/print_getdata_sction", methods=["POST", "GET"])
def print_getdata_sction():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            path = session.get('Path')
            main_data = Get_analysted_data_newst()
            print(main_data)
            return render_template('/IT/Get_data/print.html', main_data=main_data, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/IT/Tickets", methods=["POST", "GET"])
def Ticket_list_IT():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            path = session.get('Path')
            ticeket_list = Get_all_ticket_list(path)
            return render_template('/IT/Ticket/index.html', ticeket_list=ticeket_list, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/IT/Ticket_add", methods=["POST", "GET"])
def Ticket_add_IT():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            path = session.get('Path')
            return render_template('/IT/Ticket/ticket_add.html', user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/IT/Ticket_add_finall", methods=["POST", "GET"])
def Ticket_add_finall():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            username = session.get("Username")
            path = session.get('Path')
            subject = request.args.get('subject')
            desck = request.args.get('desck')
            section_to = request.args.get('section_to')
            if section_to in ['IT', 'SA', 'ACC', 'COM']:
                insert_ticket_at_start_ticket(subject, desck, section_to, username, "IT")
                return redirect('/IT/Tickets')
            else:
                return redirect('/IT/Ticket_add')
        else:
            return render_template('Not_Permission/index.html')
@app.route("/IT/Get_ticket_details", methods=["POST", "GET"])
def Get_ticket_details_IT():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            path = session.get('Path')
            t_id = request.args.get('T_id')
            main_ticket, message_ticket = Get_ticket_details(t_id)
            return render_template('/IT/Ticket/ticket_details.html', main_ticket=main_ticket, message_ticket=message_ticket, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/IT/add_ticket_message", methods=["POST", "GET"])
def add_ticket_message():

    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            username = session.get("Username")
            desck = request.args.get('desck')
            pre_id = request.args.get('T_id')
            Add_message_IT(desck, pre_id, username, 'ACC')
            return redirect(f'/IT/Get_ticket_details?T_id={pre_id}')
        else:
            return render_template('Not_Permission/index.html')



@app.route("/IT/Ticket_status", methods=["POST", "GET"])
def Ticket_status_IT():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            username = session.get("Username")
            verify = request.args.get('verify')
            pre_id = request.args.get('T_id')
            Add_status_IT(verify, pre_id)
            return redirect(f'/IT/Tickets')
        else:
            return render_template('Not_Permission/index.html')
@app.route('/IT/Invoice', methods=["POST", "GET"])
def invoice():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            list_factors = Get_factors_lookup_IT_only_factors_fro_pages(100000)
            path = session.get('Path')
            return render_template("/IT/Invoice/index.html", pre_invoice_list=list_factors,
                                   user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route('/IT/Invoice_details', methods=["POST", "GET"])
def Invoice_details():

    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            pre_invoice_id = request.args.get('P_ID')
            lookup_factors, details_factors, customer_data, seller_details = GET_details_factors_acc(pre_invoice_id)

            total_price = 0
            for i in details_factors:
                total_price = total_price + int(i[7])
            path = session.get('Path')
            return render_template('/IT/Invoice/Invoice_details.html',pre_invoice_lookup=lookup_factors, customer_details=customer_data, total_price=total_price , len_code=len(details_factors), pre_invoice_data=details_factors, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/IT/invoice_print_it", methods=["POST", "GET"])
def invoice_print_it():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            pre_invoice_id = request.args.get('id')
            lookup_factors, details_factors, customer_data, seller_details = GET_details_factors_acc(pre_invoice_id)
            invoice_total_price = 0
            for i in details_factors:
                invoice_total_price = invoice_total_price + i[7]
            invoice_total_price = "{:,}".format(invoice_total_price)
            path = session.get('Path')
            return render_template('/IT/Invoice/Invoice_Print.html',lookup_factors=lookup_factors, customer_data=customer_data, invoice_total_price=invoice_total_price , len_code=len(details_factors), details_factors=details_factors, user=session.get('Username'), pathmain=path, email=session.get('email'), seller_details=seller_details)
        else:
            return render_template('Not_Permission/index.html')

@app.route('/IT/Change_price_products_sever', methods=["POST", "GET"])
def change_price_products_to_server():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            id = request.args.get('id')
            price = request.args.get('price')
            Change_products_price_to_seve(id, price)
            return redirect('/IT/Product_list')
        else:
            return render_template('Not_Permission/index.html')

@app.route("/IT/chart_data_price", methods=["POST", "GET"])
def chart_data_price():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            id = request.args.get('id')
            chart_data = Get_analysted_data_history(id)

            return render_template('IT/Get_data/charts.html', chart_data=chart_data)
        else:
            return render_template('Not_Permission/index.html')
@app.route("/IT/chart_data_price_all", methods=["POST", "GET"])
def chart_data_price_all():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 0 or auth == 5:
            #id = request.args.get('id')'
            charts_list_data = []
            products_id_list = [[21,'404dn'],[25,'404n'],[26,'402d'],[27,'15w'],[28,'28w'],[29,'428fdn'],[31,'428dw']]
            for i in products_id_list:
                chart_data = Get_analysted_data_history(i[0])
                charts_list_data.append([i, chart_data])
            print(charts_list_data)
            return render_template('IT/Get_data/charts_all.html', charts_list_data=charts_list_data)
        else:
            return render_template('Not_Permission/index.html')
#---------------------------------------------------------------------------------------------------
#---------------------------------------------- END IT SECTION
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------- START ACCOUNITNG SECTION
#---------------------------------------------------------------------------------------------------
@app.route("/ACC")
def ACC():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            path = session.get('Path')
            tickets = Get_all_ticket_new('ACC')
            list_factors = Get_factors_lookup_ACC_with_pages(100000)
            return render_template("/ACC/index.html", list_factors=list_factors, tickets=tickets, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/ACC/Tickets", methods=["POST", "GET"])
def Ticket_list_ACC():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            path = session.get('Path')
            ticeket_list = Get_all_ticket_list('ACC')
            return render_template('/ACC/Ticket/index.html', ticeket_list=ticeket_list, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/ACC/Ticket_add", methods=["POST", "GET"])
def Ticket_add_ACC():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            path = session.get('Path')
            return render_template('/ACC/Ticket/ticket_add.html', user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/ACC/Ticket_add_finall", methods=["POST", "GET"])
def Ticket_add_finall_ACC():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            username = session.get("Username")
            path = session.get('Path')
            subject = request.args.get('subject')
            desck = request.args.get('desck')
            section_to = request.args.get('section_to')
            if section_to in ['IT', 'SA', 'ACC', 'COM']:
                insert_ticket_at_start_ticket(subject, desck, section_to, username, "ACC")
                return redirect('/ACC/Tickets')
            else:
                return redirect('/ACC/Ticket_add')
        else:
            return render_template('Not_Permission/index.html')
@app.route("/ACC/Get_ticket_details", methods=["POST", "GET"])
def Get_ticket_details_ACC():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            path = session.get('Path')
            path = 'ACC'
            t_id = request.args.get('T_id')
            main_ticket, message_ticket = Get_ticket_details(t_id)
            return render_template('/ACC/Ticket/ticket_details.html', main_ticket=main_ticket, message_ticket=message_ticket, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/ACC/add_ticket_message", methods=["POST", "GET"])
def add_ticket_message_ACC():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            username = session.get("Username")
            desck = request.args.get('desck')
            pre_id = request.args.get('T_id')
            Add_message_IT(desck, pre_id, username, 'ACC')
            return redirect(f'/ACC/Get_ticket_details?T_id={pre_id}')
        else:
            return render_template('Not_Permission/index.html')
@app.route("/ACC/Ticket_status", methods=["POST", "GET"])
def Ticket_status_ACC():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            username = session.get("Username")
            verify = request.args.get('verify')
            pre_id = request.args.get('T_id')
            Add_status_IT(verify, pre_id)
            return redirect(f'/ACC/Tickets')
        else:
            return render_template('Not_Permission/index.html')
@app.route('/ACC/Invoice', methods=["POST", "GET"])
def ACC_invoice():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            limit_id = request.args.get('limit_id')
            if limit_id is None:
                list_factors = Get_factors_lookup_ACC_with_pages(100000)
            else:
                list_factors = Get_factors_lookup_ACC_with_pages(limit_id)
            #list_factors = Get_factors_lookup_ACC_with_limits()
            path = session.get('Path')
            return render_template("/ACC/Invoice/index.html", pre_invoice_list=list_factors, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route('/ACC/Invoice_details', methods=["POST", "GET"])
def Invoice_details_ACC():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            pre_invoice_id = request.args.get('P_ID')
            lookup_factors, details_factors, customer_data, seller_details = GET_details_factors_acc(pre_invoice_id)
            total_price = 0
            for i in details_factors:
                total_price = total_price + int(i[7])
            path = session.get('Path')
            return render_template('/ACC/Invoice/Invoice_details.html',pre_invoice_lookup=lookup_factors, customer_details=customer_data, total_price=total_price , len_code=len(details_factors), pre_invoice_data=details_factors, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/ACC/invoice_print_it", methods=["POST", "GET"])
def invoice_print_it_ACC():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            pre_invoice_id = request.args.get('id')
            lookup_factors, details_factors, customer_data, seller_details = GET_details_factors_acc(pre_invoice_id)
            invoice_total_price = 0
            for i in details_factors:
                invoice_total_price = invoice_total_price + i[7]

            invoice_total_price = "{:,}".format(invoice_total_price)
            path = session.get('Path')
            return render_template('/ACC/Invoice/Invoice_Print.html',lookup_factors=lookup_factors, customer_data=customer_data, invoice_total_price=invoice_total_price , len_code=len(details_factors), details_factors=details_factors, user=session.get('Username'), pathmain=path, email=session.get('email'), seller_details=seller_details)
        else:
            return render_template('Not_Permission/index.html')
@app.route('/ACC/Pre_Invoice', methods=["POST", "GET"])
def ACC_pre_invoice():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            limit_id = request.args.get('limit_id')
            if limit_id is None:
                list_factors = Get_preinvoice_lookup_ACC_with_pages(100000)
            else:
                list_factors = Get_preinvoice_lookup_ACC_with_pages(limit_id)
            #list_factors = Get_factors_lookup_ACC_with_limits()
            path = session.get('Path')
            return render_template("/ACC/Pre_Invoice/index.html", pre_invoice_list=list_factors, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route('/ACC/Pre_Invoice_details', methods=["POST", "GET"])
def Pre_Invoice_details_ACC():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            pre_invoice_id = request.args.get('P_ID')
            lookup_factors, details_factors, customer_data, seller_details = GET_details_preinvoice_acc(pre_invoice_id)
            total_price = 0
            for i in details_factors:
                total_price = total_price + int(i[7])
            path = session.get('Path')
            return render_template('/ACC/Pre_Invoice/Invoice_details.html',pre_invoice_lookup=lookup_factors, customer_details=customer_data, total_price=total_price , len_code=len(details_factors), pre_invoice_data=details_factors, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/ACC/pre_invoice_print_it", methods=["POST", "GET"])
def pre_invoice_print_it_ACC():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            pre_invoice_id = request.args.get('id')
            lookup_factors, details_factors, customer_data, seller_details = GET_details_preinvoice_acc(pre_invoice_id)
            invoice_total_price = 0
            for i in details_factors:
                invoice_total_price = invoice_total_price + i[7]

            invoice_total_price = "{:,}".format(invoice_total_price)
            path = session.get('Path')
            return render_template('/ACC/Pre_Invoice/Invoice_Print.html',lookup_factors=lookup_factors, customer_data=customer_data, invoice_total_price=invoice_total_price , len_code=len(details_factors),seller_details=seller_details, details_factors=details_factors, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route('/ACC/invoice_sended_inovice_section', methods=["POST", "GET"])
def invoice_sended_inovice_section():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            id = request.args.get('id')
            Send_invoice_to_sended(id)
            return redirect('/ACC/Invoice')
        else:
            return render_template('Not_Permission/index.html')
@app.route('/ACC/Invoice_sended', methods=["POST", "GET"])
def Invoice_sended():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            limit_id = request.args.get('limit_id')
            if limit_id is None:
                list_factors = Get_factors_sended_lookup_ACC_with_pages(100000)
            else:
                list_factors = Get_factors_sended_lookup_ACC_with_pages(limit_id)
            #list_factors = Get_factors_lookup_ACC_with_limits()
            path = session.get('Path')
            return render_template("/ACC/Invoice_sended/index.html", pre_invoice_list=list_factors, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route('/ACC/Invoice_sended_details', methods=["POST", "GET"])
def Invoice_sended_details():

    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            pre_invoice_id = request.args.get('P_ID')
            lookup_factors, details_factors, customer_data, seller_details = GET_details_factors_acc(pre_invoice_id)
            total_price = 0
            for i in details_factors:
                total_price = total_price + int(i[7])
            path = session.get('Path')
            return render_template('/ACC/Invoice_sended/Invoice_details.html',pre_invoice_lookup=lookup_factors, customer_details=customer_data, total_price=total_price , len_code=len(details_factors), pre_invoice_data=details_factors, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route('/ACC/invoice_sended_inovice_section_okay', methods=["POST", "GET"])
def invoice_sended_inovice_section_okay():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    #just a comment for nothing for ui desginger
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            id = request.args.get('id')
            Send_invoice_to_sended_status_okay(id)
            return redirect('/ACC/Invoice_sended')
        else:
            return render_template('Not_Permission/index.html')
@app.route('/ACC/invoice_sended_inovice_section_remove', methods=["POST", "GET"])
def invoice_sended_inovice_section_remove():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            id = request.args.get('id')
            Send_invoice_to_sended_status_remove(id)
            return redirect('/ACC/Invoice_sended')
        else:
            return render_template('Not_Permission/index.html')
@app.route('/ACC/invoice_sended_inovice_section_back', methods=["POST", "GET"])
def invoice_sended_inovice_section_back():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            id = request.args.get('id')
            Send_invoice_to_sended_status_backe(id)
            return redirect('/ACC/Invoice_sended')
        else:
            return render_template('Not_Permission/index.html')
@app.route("/ACC/preinvoice_to_invoice", methods=["POST", "GET"])
def preinvoice_to_invoice():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 1 or auth == 5:
            id = request.args.get('id')
            Send_preinvoice_to_invoice(id)
            return redirect('/ACC/Invoice')
        else:
            return render_template('Not_Permission/index.html')


#---------------------------------------------------------------------------------------------------
#---------------------------------------------- END ACCOUNITNG SECTION
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------- START SALE SECTION
#---------------------------------------------------------------------------------------------------
@app.route("/SA")
def Sale_index_page():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            path = session.get('Path')
            tickets = Get_all_ticket_new('SA')
            limit_id = request.args.get('limit_id')
            if limit_id is None:
                pre_invoice_list = Get_preinvoice_lookup_SA_with_pages(10000)
                if len(pre_invoice_list) == 0:
                    limit_id=10000
                else:
                    limit_id = pre_invoice_list[0][0]
                #limit_id = 10
            else:
                limit_id = int(limit_id)
                pre_invoice_list = Get_preinvoice_lookup_SA_with_pages(limit_id)
                limit_id = limit_id
            return render_template("/SA/index.html", list_factors=pre_invoice_list, tickets=tickets, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/SA/Tickets", methods=["POST", "GET"])
def Ticket_list_SA():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            path = session.get('Path')
            ticeket_list = Get_all_ticket_list('SA')
            return render_template('/SA/Ticket/index.html', ticeket_list=ticeket_list, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/SA/Ticket_add", methods=["POST", "GET"])
def Ticket_add_SA():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            path = session.get('Path')
            return render_template('/SA/Ticket/ticket_add.html', user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/SA/Ticket_add_finall", methods=["POST", "GET"])
def Ticket_add_finall_SA():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            username = session.get("Username")
            path = session.get('Path')
            subject = request.args.get('subject')
            desck = request.args.get('desck')
            section_to = request.args.get('section_to')
            if section_to in ['IT', 'SA', 'ACC', 'COM']:
                insert_ticket_at_start_ticket(subject, desck, section_to, username, "SA")
                return redirect('/SA/Tickets')
            else:
                return redirect('/SA/Ticket_add')
        else:
            return render_template('Not_Permission/index.html')
@app.route("/SA/Get_ticket_details", methods=["POST", "GET"])
def Get_ticket_details_SA():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            path = session.get('Path')
            path = 'SA'
            t_id = request.args.get('T_id')
            main_ticket, message_ticket = Get_ticket_details(t_id)
            return render_template('/SA/Ticket/ticket_details.html', main_ticket=main_ticket, message_ticket=message_ticket, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/SA/add_ticket_message", methods=["POST", "GET"])
def add_ticket_message_SA():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            username = session.get("Username")
            desck = request.args.get('desck')
            pre_id = request.args.get('T_id')
            Add_message_IT(desck, pre_id, username, 'SA')
            return redirect(f'/SA/Get_ticket_details?T_id={pre_id}')
        else:
            return render_template('Not_Permission/index.html')
@app.route("/SA/Ticket_status", methods=["POST", "GET"])
def Ticket_status_SA():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            username = session.get("Username")
            verify = request.args.get('verify')
            pre_id = request.args.get('T_id')
            Add_status_IT(verify, pre_id)
            return redirect(f'/SA/Tickets')
        else:
            return render_template('Not_Permission/index.html')
@app.route("/SA/Customer")
def SA_Customer():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            path = session.get('Path')
            limit_id = request.args.get('limit_id')
            if limit_id is None:
                Customer_list = Get_customer_list_SA(10000)
                if len(Customer_list) == 0:
                    limit_id=10000
                else:
                    limit_id = Customer_list[0][0]
                #limit_id = 10
            else:
                limit_id = int(limit_id)
                Customer_list = Get_customer_list_SA(limit_id)
                limit_id = limit_id

            return render_template("/SA/Customer/index.html", limit_id=limit_id, Customer_list=Customer_list, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/SA/ADD_Customer")
def SA_ADD_Customers():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            path = session.get('Path')
            return render_template("/SA/Customer/ADD_Customer.html", user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/SA/Insert_Customers", methods=["POST", "GET"])
def SA_Insert_Customers():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            data = []
            data.append(request.args.get('phone'))
            data.append(request.args.get('firstname'))
            data.append(request.args.get('N_code'))
            data.append(request.args.get('E_code'))
            data.append(request.args.get('postcode'))
            data.append(request.args.get('adress'))
            print(data)
            Insert_cutomer_SA(data)
            #path = session.get('Path')
            return redirect('/SA/Customer')
        else:
            return render_template('Not_Permission/index.html')
@app.route("/SA/delet_customer", methods=["POST", "GET"])
def SA_Delet_Customer():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            id_delet = request.args.get('id')
            Delet_Customer_SA(id_delet)
            #Insert_cutomer_SA(data)
            #path = session.get('Path')
            return redirect('/SA/Customer')
        else:
            return render_template('Not_Permission/index.html')
@app.route('/SA/Pre_Invoice')
def Pre_invoice_SA():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            path = session.get('Path')
            limit_id = request.args.get('limit_id')
            if limit_id is None:
                pre_invoice_list = Get_preinvoice_lookup_SA_with_pages(10000)
                if len(pre_invoice_list) == 0:
                    limit_id=10000
                else:
                    limit_id = pre_invoice_list[0][0]
                #limit_id = 10
            else:
                limit_id = int(limit_id)
                pre_invoice_list = Get_preinvoice_lookup_SA_with_pages(limit_id)
                limit_id = limit_id

            return render_template("/SA/Pre_invoice/index.html", limit_id=limit_id, pre_invoice_list=pre_invoice_list, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route('/SA/Pre_invoice_add')
def Pre_Invoice_add_SA():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            path = session.get('Path')
            list_costumers = Get_customer_list_SA_add_preinvoice()
            return render_template("/SA/Pre_invoice/Pre_Invoice_add_customer.html", list_costumers=list_costumers, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route('/SA/Pre_invoice_add_products')
def Pre_invoice_add_products_SA():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            ID_C = request.args.get('ID_C')
            path = session.get('Path')
            list_costumers = Get_customer_details(ID_C)
            list_product = Get_products_list_SA_add_preinvoice()
            return render_template("/SA/Pre_invoice/Pre_invoice_add_products.html", ID_C=ID_C, list_product=list_product, list_costumers=list_costumers, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route('/SA/add_preinvoice_finall_check')
def add_preinvoice_finall_check_sa():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            ID_C = request.args.get('ID_C')
            NAME_C = request.args.get('NAME_C')
            products = request.args.getlist('product[]', type=str)
            products_number = request.args.getlist('product_number[]', type=str)
            product_name_p = request.args.getlist('product_name_p[]', type=str)
            product_number_p = request.args.getlist('product_number_p[]', type=str)
            product_price_p = request.args.getlist('product_price_p[]', type=str)
            list_costumers = Get_customer_details(ID_C)
            list_products = []
            list_products_p = []
            for i in range(0,len(product_name_p)):
                print("{:,}".format(int(product_price_p[i])))
                list_products_p.append([product_name_p[i], product_number_p[i], "{:,}".format(int(product_price_p[i])), product_price_p[i]])
            for i in range(0,len(products)):
                plist = Get_product_add_preinvoice(products[i])
                list_products.append([products[i], plist[0][1], products_number[i], "{:,}".format(plist[0][2]/10), plist[0][2]])
            print(list_products_p)
            return render_template('SA/Pre_invoice/Finall_check.html',ID_C=ID_C, NAME_C=NAME_C, list_costumers=list_costumers, list_products=list_products, list_products_p=list_products_p)
        else:
            return render_template('Not_Permission/index.html')
@app.route('/SA/add_preinvoice_finall')
def Add_preinvoice_finall_SA():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            ID_C = request.args.get('ID_C')
            NAME_C = request.args.get('NAME_C')
            products = request.args.getlist('product[]', type=str)
            products_number = request.args.getlist('product_number[]', type=str)
            product_name_p = request.args.getlist('product_name_p[]', type=str)
            product_number_p = request.args.getlist('product_number_p[]', type=str)
            product_price_p = request.args.getlist('product_price_p[]', type=str)
            Add_preinvoice_SA(ID_C, products, products_number, product_name_p, product_number_p, product_price_p, session.get("Username"), NAME_C)

            return redirect('/SA/Pre_Invoice')
        else:
            return render_template('Not_Permission/index.html')
@app.route('/SA/Pre_Invoice_details', methods=["POST", "GET"])
def Pre_Invoice_details_SA():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            pre_invoice_id = request.args.get('P_ID')
            lookup_factors, details_factors, customer_data, seller_details = GET_details_preinvoice_acc(pre_invoice_id)
            total_price = 0
            for i in details_factors:
                total_price = total_price + int(i[7])
            path = session.get('Path')
            return render_template('/SA/Pre_invoice/Invoice_details.html',pre_invoice_lookup=lookup_factors, customer_details=customer_data, total_price=total_price , len_code=len(details_factors), pre_invoice_data=details_factors, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/SA/pre_invoice_print_it", methods=["POST", "GET"])
def pre_invoice_print_it_SA():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            pre_invoice_id = request.args.get('id')
            lookup_factors, details_factors, customer_data, seller_details = GET_details_preinvoice_acc(pre_invoice_id)
            invoice_total_price = 0
            for i in details_factors:
                invoice_total_price = invoice_total_price + i[7]

            invoice_total_price = "{:,}".format(invoice_total_price)
            path = session.get('Path')
            return render_template('/ACC/Pre_Invoice/Invoice_Print.html',lookup_factors=lookup_factors, customer_data=customer_data, invoice_total_price=invoice_total_price , len_code=len(details_factors),seller_details=seller_details, details_factors=details_factors, user=session.get('Username'), pathmain=path, email=session.get('email'))
        else:
            return render_template('Not_Permission/index.html')
@app.route("/SA/preinvoice_delet_it", methods=["POST", "GET"])
def preinvoice_delet_SA():
    if not session.get("Username"):
        return render_template("/Login/Login_v4/index.html")
    else:
        auth = session.get('Access_level')
        if auth == 4 or auth == 5:
            pre_invoice_id = request.args.get('id')
            delet_preinvoice_it(pre_invoice_id)
            return redirect('/SA/Pre_Invoice')
        else:
            return render_template('Not_Permission/index.html')

#---------------------------------------------------------------------------------------------------
#---------------------------------------------- END SALE SECTION
#---------------------------------------------------------------------------------------------------



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=1000)

