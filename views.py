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

def make_connection_cursor():
    return mysql.connector.connect(user=USER, password=PASSWORD,
                                host=HOST,
                                database=DATABASE).cursor()



@app.route('/', methods=['GET'])
def index():
    """This displays the index page for OurVLE it shows the courses 
        to the guess user
    """
    pass


@app.route('/login',methods =['POST','GET'])
def login():
    """1st check if the user is already signed in"""
    if current_user.is_authenticated:
        respr =  jsonify({"result":"Successful Login"})
        return make_response(respr,200)
    
    form = Login()
    if request.method == 'POST'  and form.validate_on_submit():
        userID = form.userID.data
        password = form.Password.data

        try:
            cursor = make_connection_cursor()
            sql_stmt = "SELECT password FROM Account WHERE AID = %(uID)s"
            cursor.execute(sql_stmt,{'uID':userID})
            userPassword = cursor.fetchone()

            if user:
                if sha256_crypt.verify(userPassword, password):
                        '''Prob hav to use session storage
                        Or talk to Stone about using a user object in order to store login
                        state'''

                pass
            else:
                return make_response({'error':"Invalid Credentials, Please try again."},401)
                


        except Exception as ex:
            return make_response({'error': str(ex)}, 400)

        '''Complete here'''

    
    
