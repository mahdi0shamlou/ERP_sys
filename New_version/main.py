from flask import Flask, render_template, redirect, request, session, json
from flask_session.__init__ import Session
from Login.main import Check_login #this method do work for login section
from Login.logout import insert_log_login_logout #this method do work for login section
from IT.Products.Get_product_list import Get_product_list  #this method get product from local database

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
        return render_template("/IT/Login_v4/index.html")
    else:
        path = session.get('Path')
        return render_template("/IT/index.html", user=session.get('Username'), pathmain=path, email=session.get('email'))

@app.route("/IT/Product_list")
def IT_Product_list():
    if not session.get("Username"):
        return render_template("/IT/Login_v4/index.html")
    else:
        path = session.get('Path')
        Product_list = Get_product_list()
        return render_template("/IT/Product_list/index.html", user=session.get('Username'), pathmain=path, email=session.get('email'), Product_list=Product_list)
@app.route("/IT/Customers")
def IT_Customers():
    if not session.get("Username"):
        return render_template("/IT/Login_v4/index.html")
    else:
        path = session.get('Path')
        return render_template("/IT/Customer/index.html", user=session.get('Username'), pathmain=path, email=session.get('email'))

@app.route("/IT/Update_all_data_online_from_server")
def IT_Update_data():
    if not session.get("Username"):
        return render_template("/IT/Login_v4/index.html")
    else:
        return redirect('/')
#---------------------------------------------------------------------------------------------------
#---------------------------------------------- END IT SECTION
#---------------------------------------------------------------------------------------------------





if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

