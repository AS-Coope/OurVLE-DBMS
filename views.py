from flask import Flask, request, make_response,jsonify,session
from flask_login import current_user, login_user,login_required, logout_user
from werkzeug.security import check_password_hash
from passlib.hash import sha256_crypt
import mysql.connector
from forms_OurVLE import *



"""
snippet here
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


# Create a connection class here 

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
                cursor.close()
                return make_response(errors,400)
                

        except Exception as ex:
            return make_response({'error': "There has been an error in communicating with the database when attempting to Login. Please contact your system administrator"}, 400)
    
    # If request is not post render the template for logging in below
    '''Complete here'''


        
@app.route('/employee-registration',methods=['GET', 'POST'])
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
            sql_stmt = "INSERT into LECTURER (lID,Fname,Lname,lPassword) VALUES( %(lectID)s,  %(lectFname)s, %(lectLname)s,  %(lectpwd)s);"  # Used to secure SQL statements to prevent injection
            cursor.execute(sql_stmt,{'lectID':LectID, 'lectFname':fName,'lectLname':lName,'lectpwd':hashedPassword})
            cursor.close()
            return make_response({'success':'Your account has been created.'},201)

        except Exception as ex:
            return make_response({'error': "There has been an error in communicating with the database when attempting to creating your account. Please contact your system administrator"}, 400)
    
    '''If the request is GET return the template to create the account'''
    

        

@app.route('/student-registration',methods=['GET', 'POST'])
def studentRegister():

    form = StudentRegistration()
    if request.method == 'POST'  and form.validate_on_submit():
        fName = form.Fname.data
        lName = form.Lname.data
        stuID = form.StudentID.data
        pwd = form.Passowrd.data
        
        hashedPassword = sha256_crypt.hash(pwd)
        '''complete here'''
        try:
            cursor = make_connection_cursor()
            sql_stmt = "INSERT into Student (lID,Fname,Lname,sPassword) VALUES( %(sID)s,  %(Fname)s,%(Lname)s,  %(lectpwd)s);"  # Used to secure SQL statements to prevent injection
            cursor.execute(sql_stmt,{'lectID':stuID, 'Fname':fName,'Lname':lName,'sPassword':hashedPassword})
            cursor.close()
            return make_response({'success':'Your account has been created.'},201)

        except Exception as ex:
            return make_response({'error': "There has been an error in communicating with the database when attempting to create your account. Please contact your system administrator"}, 400)
    
    '''If the request is GET return the template to create the account'''


    """_summary_
        Creates a Course
    Returns:
        Unauthorised: Informs the user that they do not have the prvilage to access the requested content
        Success: Informs the user that a particular course has been created
        error: Appropriate error message
    """
@app.route('/create-course',methods=['GET','POST'])
def createCourse():

    '''If the user is not signed in as an admin the person is not allowed to continue'''

    if not session['admin_id']:
        return make_response({'Unauthorised':'You are not authorised to execute the requested service'},401)
    

    form = CreateCourse()
    if request.method == 'POST'  and form.validate_on_submit():

        cCode = form.CourseCode.data
        cTitle = form.CourseName.data
        try:
            cursor = make_connection_cursor()
            sql_stmt = "INSERT into Course (cName,cCode) VALUES(%(cc)s, %(ct)s);"
            cursor.execute(sql_stmt,{'cc':cCode,'ct':cTitle})
            cursor.close()
            return make_response({'success':f'The course, {cTitle} has been created.'},201)
        except Exception as ex:
            return make_response({'error': f"There has been an error in communicating with the database when attempting to creat the course {cTitle}. Please contact your system administrator"}, 400)
        
    '''If the request is GET return the template to create the account'''

    """_summary_
        Retrieve all the courses
    Returns:
        Success: list of courses ad dictionary objects
        Error: Appropriate error message
    """
@app.route('/get-courses',methods=['GET'])
def getCourses():
    try:
        cursor = make_connection_cursor()
        sql_stmt = "SELECT * from Course;"
        cursor.execute(sql_stmt)
        course_list = []

        for cName, cCode in cursor:
            crse ={}
            crse['courseCode'] = cCode
            crse['courseName'] = cName
            course_list.append(crse)
        cursor.close()

        return make_response(course_list,200)   
    
        
    except Exception as ex:
        return make_response({'error':'There has been an error in communicating with the database while retrieving the course. Please contact your sysem administrator'},400)
    

    
@app.route('/get-course/<studentId>')
def getStudentCourse(studentId):

    try:
        cursor = make_connection_cursor()

        ''''To complete this query it should search in the enrollment table for the student ID
            then with the cIDs that it have -if any- search for the course titles'''
        
        sql_stmt = "SELECT DISTINCT cID FROM enrollment WHERE sID  =%(sID)s;" # select cIDs for student
        courses = cursor.execute(sql_stmt,{'sID':studentId})

        course_list = [cName for cName in courses]
        cursor.close()
        
        if course_list:
            return make_response({"success":course_list},200)
        else:
            return make_response({'Info': []},204)

    except Exception as ex:
        return make_response({'error':f'There has been an error in communicating with the database while retrieving the Student, {studentId} courses. Please contact your sysem administrator'},400)



"""_summary_
    This function is designed to Retrieve courses taught by a particular lecturer 
Returns:
    sucess: List of all the courses taught by the instructor
    info: An empty list if the lecturer doesnt teach any courses
    error: Appropriate error message
"""


@app.route('/LecturerCourses/<lectID>')
def lecturerCourses(lectID):
    try:
        cursor = make_connection_cursor()

        ''''To complete this query it should search in the LectOfCourse table for the lect ID
            then with the lectID that it have -if any- search for the course titles'''
        
        sql_stmt = "SELECT DISTINCT cID FROM enrollment WHERE sID  =%(lectID)s;" # select cIDs for Lecturer
        coursesLectured = cursor.execute(sql_stmt,{'lectID':lectID})

        courses_lectured_list = [cName for cName in coursesLectured]

        if courses_lectured_list:
            return make_response({"success":courses_lectured_list},200)
        else:
            return make_response({'Info': []},204)


    except Exception as ex:
        return make_response({'error':f'There has been an error in communicating with the database while retrieving '\
                              'the courses for a lecturer with ID, {lectID}.'\
                              ' Please try again if the issue persist please contact your sysem administrator'},400)



 



    
    






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
