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
DATABASE = 'db_name'

app = Flask(__name__)


class connectionHandler:

    def __init__(self) -> None:
        self.connection = self.make_connection_cursor()
        self.cursor =  self.connection.cursor()

    @classmethod
    def make_connection_cursor(self):
        return mysql.connector.connect(user=USER, password=PASSWORD,
                                host=HOST,
                                database=DATABASE)
    
    def close_cursor(self):
        self.cursor.close()
    
    def close_connection(self):
        self.connection.close()
    
    def close_cursor_and_connection(self):
        self.cursor.close()
        self.connection.close()



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
            conn = connectionHandler()
            sql_stmt = "SELECT password FROM Account WHERE AID = %(uID)s;"  # Used to secure SQL statements to prevent injection
            conn.cursor.execute(sql_stmt,{'uID':userID})
            #conn.cursor.commit() # may need to do this
            userPassword =  conn.cursor.fetchone()

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
                    'errors': form_errors(form)
                }
                conn.close_cursor_and_connection()
                return make_response(errors,400)
                
        except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
        except Exception as ex:
            conn.close_cursor_and_connection()
            return make_response({'error': "There has been an error in communicating with the database when attempting to Login. Please contact your system administrator"}, 503)
    
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
            conn = connectionHandler()
            sql_stmt = "INSERT into LECTURER (lID,Fname,Lname,lPassword) VALUES( %(lectID)s,  %(lectFname)s, %(lectLname)s,  %(lectpwd)s);"  # Used to secure SQL statements to prevent injection
            conn.cursor.execute(sql_stmt,{'lectID':LectID, 'lectFname':fName,'lectLname':lName,'lectpwd':hashedPassword})
            conn.cursor.commit()
            conn.close_cursor_and_connection()
            return make_response({'success':'Your account has been created.'},201)
        
        except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
        except Exception as ex:
            conn.close_cursor_and_connection()
            return make_response({'error': "There has been an error in communicating with the database when attempting to creating your account. Please contact your system administrator"}, 503)
    
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
            conn = connectionHandler()
            sql_stmt = "INSERT into Student (lID,Fname,Lname,sPassword) VALUES( %(sID)s,  %(Fname)s,%(Lname)s,  %(lectpwd)s);"  # Used to secure SQL statements to prevent injection
            conn.cursor.execute(sql_stmt,{'lectID':stuID, 'Fname':fName,'Lname':lName,'sPassword':hashedPassword})
            conn.cursor.commit()
            conn.close_cursor_and_connection()
            return make_response({'success':'Your account has been created.'},201)
        except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
        
        except Exception as ex:
            return make_response({'error': "There has been an error in communicating with the database when attempting to create your account. Please contact your system administrator"}, 503)
    
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
            conn = connectionHandler()
            sql_stmt = "INSERT into Course (cName,cCode) VALUES(%(cc)s, %(ct)s);"
            conn.cursor.execute(sql_stmt,{'cc':cCode,'ct':cTitle})
            conn.cursor.commit()
            conn.close_cursor_and_connection()
            return make_response({'success':f'The course, {cTitle} has been created.'},201)

        except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
        
        except Exception as ex:
            conn.close_cursor_and_connection()
            return make_response({'error': f"There has been an error in communicating with the database when attempting to creat the course {cTitle}. Please contact your system administrator"}, 503)
        
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
        conn = connectionHandler()
        sql_stmt = "SELECT * from Course;"
        conn.cursor.execute(sql_stmt)
        course_list = []

        for cName, cCode in conn.cursor:
            crse ={}
            crse['courseCode'] = cCode
            crse['courseName'] = cName
            course_list.append(crse)
        conn.close_cursor_and_connection()

        return make_response(course_list,200)   
    
    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
        
    except Exception as ex:
        return make_response({'error':'There has been an error in communicating with the database while retrieving the course. Please contact your sysem administrator'},503)
    

    
@app.route('/get-course/<studentId>',methods=['GET'])
def getStudentCourse(studentId):

    try:
        conn = connectionHandler()

        ''''To complete this query it should search in the enrollment table for the student ID
            then with the cIDs that it have -if any- search for the course titles'''
        
        sql_stmt = "SELECT DISTINCT cID FROM enrollment WHERE sID  =%(sID)s;" # select cIDs for student
        conn.cursor.execute(sql_stmt,{'sID':studentId})

        course_list = [cName for cName in conn.cursor]
        conn.close_cursor_and_connection()
        
        if course_list:
            return make_response({"success":course_list},200)
        else:
            return make_response({'Info': []},204)

    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        return make_response({'error':f'There has been an error in communicating with the database while retrieving the Student, {studentId} courses. Please contact your sysem administrator'},503)



"""_summary_
    This function is designed to Retrieve courses taught by a particular lecturer 
Returns:
    sucess: List of all the courses taught by the instructor
    info: An empty list if the lecturer doesnt teach any courses
    error: Appropriate error message
"""


@app.route('/LecturerCourses/<lectID>',methods=['GET'])
def lecturerCourses(lectID):
    try:
        conn = connectionHandler()

        ''''To complete this query it should search in the LectOfCourse table for the lect ID
            then with the lectID that it have -if any- search for the course titles'''
        
        sql_stmt = "SELECT DISTINCT cID FROM enrollment WHERE sID  =%(lectID)s;" # select cIDs for Lecturer
        conn.cursor.execute(sql_stmt,{'lectID':lectID})

        courses_lectured_list = [cName for cName in conn.cursor]

        if courses_lectured_list:
            return make_response({"success":courses_lectured_list},200)
        else:
            return make_response({'Info': []},204)

    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        return make_response({'error':f'There has been an error in communicating with the database while retrieving '\
                              'the courses for a lecturer with ID, {lectID}.'\
                              ' Please try again if the issue persist please contact your sysem administrator'},503)


@app.route('/assigned-Lecturer-to-course',methods=['GET','POST'])
def assignLecturer(lectID):
    form = AssignLecturerToCourse()
    
    try:
        conn = connectionHandler()
        

        if request.method == 'POST' and form.validate_on_submit():
            lectID = form.LecturerOptions.data
            courseID = form.CourseOptions.data

            sql_stmt = "SELECT COUNT(lID) FROM LectOfCourse WHERE cID  =%(courseID)s;"
            conn.cursor.execute(sql_stmt,{'courseID':courseID})
            count = conn.cursor.fetchone()[0]
            if count > 0:
                return make_response({'error':'There is already a lecturer assigned to the Selected course.'})
            else:
                sql_insert_stmt = "INSERT INTO LectOfCourse(cID,lID) VALUES(%(cid)s, %(lectID)s);"
                conn.cursor.execute(sql_insert_stmt,{'cid':courseID,'lid':lectID})
                conn.cursor.commit()

                conn.close_cursor_and_connection()

                return make_response({'success':f'The course has been assigned a lecturer'})

        """If the request is GET"""    
        
        list_of_lecturers = [] # stores tuple with lect fullname and ID
        list_of_courses = [] # stores tuple with course title and course ID

        # populate the drop down boxes with the lecturer names and course title
        conn.cursor.execute("SELECT * FROM Lecturer;")
        for fName, lName, lID in conn.cursor:
            list_of_lecturers.append((f'{fName} {lName}',lID))

        conn.cursor.execute("SELECT * FROM Course;")
        for cName, cID in conn.cursor:
            list_of_courses.append((cName,cID))
        
        form.LecturerOptions.choices = list_of_lecturers
        form.CourseOptions.choices = list_of_courses

        """return the rendered template along with the form eg. return render_template('assign.html',form = form)"""

    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        return make_response({'error':'An error occurred when attempting to update the course information'},503)



@app.route('/course-registration',methods=['GET','POST'])
def courseRegistration():

    form = CourseRegistration()

    try:
        conn = connectionHandler()
        if request.method == 'POST':
            if form.validate():
                studentID = form.StudentID.data
                courseID = form.CourseOptions.data

                #check if the student is already registered
                sql_stmt_check_if_alrady_reg = "select IF((SELECT COUNT(sID) FROM LectOfCourse WHERE cID = %(courseID)s AND sID = %(studentID)s) > 0, 'Yes', 'No') as Result;"
                conn.cursor.execute(sql_stmt_check_if_alrady_reg,{'courseID':courseID,'studentID':studentID})
                
                
                if conn.cursor.fetchone() == 'Yes':
                    return make_response({'error': "the Student is already registerd for the selected course"},400)
                
                #check to ensure the student is registered in no more that 6 courses
                sql_stmt_check_course_limit = "select IF((SELECT COUNT(cID) FROM LectOfCourse WHERE sID = %(studentID)s) > 5, 'Yes', 'No') as Result;"
                conn.cursor.execute(sql_stmt_check_course_limit,{'studentID':studentID})

                if conn.cursor.fetchone() == 'Yes':
                    return make_response({'error': "the student is already registered for the maximum of 6 credits"},400)
                
                #if all requirements are met commit
                sql_stmt_register = "INSERT INTO StudOfCourse (sID,cID) VALUES(%(stuID)s, %(crsID)s);"
                conn.cursor.execute(sql_stmt_register,{'stuID':studentID,'crsID':courseID})
                conn.cursor.commit()

                return make_response({'success':"The student has been registered for the course"},200)

            else:
                errors = {
                    'errors': form_errors(form)
                }
                conn.close_cursor_and_connection()
                return make_response(errors,400)

        

        """If Request is GET"""
        list_of_courses = [] # stores tuple with course title and course ID

        # populate the drop down boxes with the  course titles

        conn.cursor.execute("SELECT * FROM Course;")
        for cName, cID in conn.cursor:
            list_of_courses.append((cName,cID))
        
        form.CourseOptions.choices = list_of_courses

        """render the template with the form"""

    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        return make_response({'error':'An error occurred when attempting to update the course information'},503)


@app.route('/get-students-for-course',methods=['GET','POST'])
def getRegisteredStudents():

    form  = GetRegisteredStudents()

    try:
        conn = connectionHandler()
        if request.method == "POST":
            if form.validate():

                courseID = form.CourseOptions.data

                sql_stmt = "SELECT DISTINCT sID FROM StudOfCourse WHERE cID = %(crseID)s;"
                conn.cursor.execute(sql_stmt,{'crseID':courseID})

                course_list= []

                for cID in conn.cursor:
                    course_list.append(cID)
                
                return make_response({'success':course_list},200)  
            else:
                errors = {
                    'errors': form_errors(form)
                }
                conn.close_cursor_and_connection()
                return make_response(errors,400)                
    

        if request.method == 'GET':
            
            list_of_courses = [] # stores tuple with course title and course ID

            # populate the drop down boxes with the  course titles

            conn.cursor.execute("SELECT * FROM Course;")
            for cName, cID in conn.cursor:
                list_of_courses.append((cName,cID))
            
            form.CourseOptions.choices = list_of_courses

            """render the template with the form fields"""
    
    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        return make_response({'error':'An error occurred when attempting to retrieve student information'},503)
    
@app.route('/get-calendar-events',methods=['GET','POST'])
def getEvents():

    form  = GetCalendarEvents()
    try:
        conn = connectionHandler()
        if request.method == "POST":
            if form.validate():

                courseID = form.CourseOptions.data

                """The Add query to acess CalendarEvents and CalEventOfCourse"""
                sql_stmt = ""
                conn.cursor.execute(sql_stmt,{'crseID':courseID})

                events= []

                for calEvName,evDate in conn.cursor:
                    event ={}
                    event['evDate']  = evDate
                    event['calEvName'] = calEvName
                    events.append(event)
                
                return make_response({'success':events},200)
            else:
                errors = {
                    'errors': form_errors(form)
                }
                conn.close_cursor_and_connection()
                return make_response(errors,400)

        
        

        """GET Request"""
        list_of_courses = [] # stores tuple with course title and course ID

            # populate the drop down boxes with the  course titles

        conn.cursor.execute("SELECT * FROM Course;")
        for cName, cID in conn.cursor:
            list_of_courses.append((cName,cID))
        
        form.CourseOptions.choices = list_of_courses

        # return rendered template with form

    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        return make_response({'error':'An error occurred when attempting to retreive calendar Events'},503)
    


@app.route('/get-calendar-events-student',methods=['GET','POST'])
def getStudentEvents():
    form = getStudentCalendarEvents()

    try:
        conn = connectionHandler()

        if request.method == 'POST':
            if form.validate():
                courseID = form.CourseOptions.data
                studentID = form.student.data
                
                """The Add query to acess CalendarEvents and CalEventOfCourse for a particular Student"""
                sql_stmt = ""
                conn.cursor.execute(sql_stmt,{'crseID':courseID,'studentID':studentID})

                events= []

                for calEvName,evDate in conn.cursor:
                    event ={}
                    event['evDate']  = evDate
                    event['calEvName'] = calEvName
                    events.append(event)
                
                return make_response({'success':events},200)

            
            else:
                errors = {
                    'errors': form_errors(form)
                }
                conn.close_cursor_and_connection()
                return make_response(errors,400)
            
        
        """GET request"""
        list_of_courses = [] # stores tuple with course title and course ID

            # populate the drop down boxes with the  course titles
        """Write SQL to select course based of student enrollment Insert below"""
        conn.cursor.execute("")
        for cName, cID in conn.cursor:
            list_of_courses.append((cName,cID))
        
        form.CourseOptions.choices = list_of_courses

        # return rendered template with form


    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        return make_response({'error':'An error occurred when attempting to retreive calendar Events'},503)
    



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
