from flask import Flask, request, render_template,session,redirect,url_for,make_response
from markupsafe import escape

app = Flask(__name__)
app.secret_key = "mnbvcxzlkj"

@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == 'POST':
        usr = request.form['user']
        pwd = request.form['pwd']
        usrname = request.cookies.get("username")
        password = request.cookies.get("password")
        if usr == usrname and pwd == password:
            return render_template('index.html',cs=usrname)    
    return render_template('login.html')

@app.route("/reg/",methods=['GET','POST'])
def reg():
    if request.method == "POST":
        name = request.form['name']
        mail = request.form['email']
        pwd = request.form['pwd']
        resp = make_response(render_template("reg.html"))
        resp.set_cookie("username",name)
        resp.set_cookie("password",pwd)
        return resp
    
    return render_template("reg.html")
