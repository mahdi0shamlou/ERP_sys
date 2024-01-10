from flask import Flask, render_template, redirect, request, session, json
from flask_session.__init__ import Session
from Login.main import Check_login
from Login.logout import insert_log_login_logout


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









if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

