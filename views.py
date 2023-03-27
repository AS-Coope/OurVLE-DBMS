from flask import Flask, request, make_response,jsonify
from flask_login import current_user, login_user,login_required, logout_user
from werkzeug.security import check_password_hash
from passlib.hash import sha256_crypt
import mysql.connector
from forms_OurVLE import *



"""
password = sha256_crypt.hash("password")
password2 = sha256_crypt.hash("password")

print(password)
print(password2)

print(sha256_crypt.verify("password", password))
"""






USER = 'enter user'
PASSWORD = 'enter password here'
HOST = 'localhost'
DATABASE = 'lab3_3161'

app = Flask(__name__)




@app.route('/', methods=['GET'])
def index():
    """This displays the index page for OurVLE it shows the courses 
        to the guess user
    """
    pass


@app.route('/login',methods =['POST','GET'])
def login():
    if current_user.is_authenticated:
        respr =  jsonify({"result":"Successful Login"})
        return make_response(respr,200)
    
    form = Login()
    if request.method == 'POST'  and form.validate_on_submit():
        username = form.UID.data
        password = form.Password.data
        '''Complete here'''

    
    
