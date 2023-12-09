import os
from flask import Flask,jsonify,request,render_template,flash,redirect,url_for
from flask_mysqldb import MySQL
from users import create_user,get_users,get_user,update_user,delete_user
from database import set_mysql
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Required
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_PORT"] = int(os.getenv("MYSQL_PORT"))
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")
# Extra configs, optional but mandatory for this project:
app.config["MYSQL_CURSORCLASS"] = os.getenv("MYSQL_CURSORCLASS")
app.config["MYSQL_AUTOCOMMIT"] = True if os.getenv("MYSQL_AUTOCOMMIT") == "true" else False

mysql = MySQL(app)
set_mysql(mysql)

app.secret_key = os.getenv("FLASK_SECRET_KEY", "your_secret_key_here")


app.template_folder = "template"
app.static_folder = "static"
@app.route("/")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup", methods=["POST"])
def signup():
    name = request.form.get("hello")
    age = request.form.get("age")
    email = request.form.get("email")
    password = request.form.get("password")

       
    user_id = create_user(name, age, email, password)
    
    return redirect(url_for("login"))



 



