from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/hello/')
def hello():
    return 'Hello, World!'


@app.route("/<firstname>/")
def helloworld(firstname):
    fn=firstname
    return render_template("index.html",fs=fn)


@app.route("/user", methods = ["POST", "GET"])
def user_detail():
    if request.method == "GET":
        return "list all details"
    elif request.method == "POST":
        return "Creating a new user"
    

@app.route("/user/<int:usr_id>", methods = ["GET", "POST", "PATCH", "DELETE"])
def user_data(usr_id):
    if request.method == "GET":
        return f"list all details of {usr_id}"
    elif request.method == "POST":
        return f"Creating a new user {usr_id}"
    elif request.method == "PATCH":
        return f"Updating data of {usr_id}"





