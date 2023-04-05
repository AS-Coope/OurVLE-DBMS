from flask import Flask, request, make_response,jsonify,session
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
  
    form = Login()
    if request.method == 'POST'  and form.validate_on_submit():
        session.pop('user_id',None) # Logs out user if present once login request sent
        userID = form.userID.data
        Enteredpassword = form.Password.data

        try:
            cursor = make_connection_cursor()
            sql_stmt = "SELECT password FROM Account WHERE AID = %(uID)s;"  # Used to secure SQL statements to prevent injection
            cursor.execute(sql_stmt,{'uID':userID})
            userPassword = cursor.fetchone()

            if userPassword:
                if sha256_crypt.verify(userPassword, Enteredpassword):
                        #Login the user
                        session['user_id'] = userID

                        ''' Could also redirect the user to a home page here'''

                        return make_response({'result': "Succeessful Login"},200)
                # The password is Incorrect
                else:
                    return make_response({'result': "Login unsuccessful Please check your password and/or your username"},401)
            # There are other errors in the form that have stopped it from being processed
            else:
                errors = {
                    'errrors': form_errors(form)
                }
                return make_response(errors,400)
                

            cursor.close()
        except Exception as ex:
            return make_response({'error': "There has been an error in communicating with the database when attempting to Login. Please contact your system administrator"}, 400)
    
    # If request is not post render the template for logging in below
    '''Complete here'''


        
@app.route('/Employee-registration',methods=['GET', 'POST'])
def empRegister():

    form = LecturerRegistration()
    if request.method == 'POST'  and form.validate_on_submit():
        fName = form.Fname.data
        lName = form.Lname.data
        LectID = form.LectureID.data
        pwd = form.Passowrd.data
        
        hashedPassword = sha256_crypt.hash(pwd)

        try:
            cursor = make_connection_cursor()
            sql_stmt = "INSERT into LECTURER (lID,Lname,lPassword) VALUES( %(lectID)s,  %(lectName)s,  %(lectpwd)s);"  # Used to secure SQL statements to prevent injection
            cursor.execute(sql_stmt,{'lectID':LectID, 'lectName':fName,'lectpwd':hashedPassword})
            return make_response({'success':'Your account has been created.'},201)

        except Exception as ex:
            return make_response({'error': "There has been an error in communicating with the database when attempting to Login. Please contact your system administrator"}, 400)
    
    '''IF the request is GET return the template to create the account'''
    

        

@app.route('/Student-registration',methods=['GET', 'POST'])
def empRegister():

    form = StudentRegistration()
    if request.method == 'POST'  and form.validate_on_submit():
        fName = form.Fname.data
        lName = form.Lname.data
        LectID = form.StudentID.data
        pwd = form.Passowrd.data
        
        hashedPassword = sha256_crypt.hash(pwd)
        '''complete here'''
        try:
            cursor = make_connection_cursor()
            sql_stmt = "INSERT into Student (lID,Lname,lPassword) VALUES( %(lectID)s,  %(lectName)s,  %(lectpwd)s);"  # Used to secure SQL statements to prevent injection
            cursor.execute(sql_stmt,{'lectID':LectID, 'lectName':fName,'lectpwd':hashedPassword})
            return make_response({'success':'Your account has been created.'},201)

        except Exception as ex:
            return make_response({'error': "There has been an error in communicating with the database when attempting to Login. Please contact your system administrator"}, 400)
    

 



    
    






    """Helper Functions"""


# Here we define a function to collect form errors from Flask-WTF
# whice returns a collection of error which can be displayed to the user on the front
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages
