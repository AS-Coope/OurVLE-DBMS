from app import app
from flask import Flask, render_template, request, make_response,jsonify,session
# from flask_login import current_user , login_user,login_required, logout_user
# from werkzeug.security import check_password_hash
# from passlib.hash import sha256_crypt
import mysql.connector
# from app.forms_OurVLE import *



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
    return render_template('base.html')


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
                return make_response(errors,422)
                
        except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
        except Exception as ex:
            conn.close_cursor_and_connection()
            return make_response({'error': "There has been an error in communicating with the database when attempting to Login. Please contact your system administrator"}, 503)
    
    # If request is not post render the template for logging in below
    '''Complete here'''


        
@app.route('registration/employee-registration',methods=['GET', 'POST'])
def empRegister():

    form = LecturerRegistration()
    if request.method == 'POST'  and form.validate_on_submit():
        fName = form.Fname.data
        mName = form.mName.data
        lName = form.Lname.data
        LectID = form.LectureID.data
        pwd = form.Passowrd.data
        
        hashedPassword = sha256_crypt.hash(pwd)

        try:
            conn = connectionHandler()
            sql_stmt = "INSERT into LECTURER (lID,Fname, Mname,Lname,lPassword) VALUES( %(lectID)s,  %(lectFname)s, %(lectMname)s, %(lectLname)s,  %(lectpwd)s);"  # Used to secure SQL statements to prevent injection
            conn.cursor.execute(sql_stmt,{'lectID':LectID, 'lectFname':fName,'lectMname':mName , 'lectLname':lName,'lectpwd':hashedPassword})
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
    

        

@app.route('registration/student-registration',methods=['GET', 'POST'])
def studentRegister():

    form = StudentRegistration()
    if request.method == 'POST'  and form.validate_on_submit():
        fName = form.Fname.data
        mName = form.mName.data
        lName = form.Lname.data
        stuID = form.StudentID.data
        pwd = form.Passowrd.data
        
        hashedPassword = sha256_crypt.hash(pwd)
        '''complete here'''
        try:
            conn = connectionHandler()
            sql_stmt = "INSERT into Student (lID,Fname,Mname,Lname,sPassword) VALUES( %(sID)s,  %(Fname)s, %(Mname)s, %(Lname)s,  %(lectpwd)s);"  # Used to secure SQL statements to prevent injection
            conn.cursor.execute(sql_stmt,{'lectID':stuID, 'Fname':fName, 'Mname': mName, 'Lname':lName,'sPassword':hashedPassword})
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
@app.route('course/create',methods=['GET','POST'])
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
@app.route('courses/',methods=['GET'])
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
    

    
@app.route('/courses/<studentId>',methods=['GET'])
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


@app.route('courses/<lectID>',methods=['GET'])
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
        conn.close_cursor_and_connection()
        return make_response({'error':f'There has been an error in communicating with the database while retrieving '\
                              'the courses for a lecturer with ID, {lectID}.'\
                              ' Please try again if the issue persist please contact your sysem administrator'},503)


@app.route('course/assign',methods=['GET','POST'])
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
                conn.close_cursor_and_connection()
                return make_response({'error':'There is already a lecturer assigned to the Selected course.'},304)
            else:
                sql_insert_stmt = "INSERT INTO LectOfCourse(cID,lID) VALUES(%(cid)s, %(lectID)s);"
                conn.cursor.execute(sql_insert_stmt,{'cid':courseID,'lid':lectID})
                conn.cursor.commit()

                conn.close_cursor_and_connection()

                return make_response({'success':f'The course has been assigned a lecturer'},201)

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
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to update the course information'},503)



@app.route('course/registration',methods=['GET','POST'])
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
                return make_response(errors,422)

        

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
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to update the course information'},503)


@app.route('course/enrollment',methods=['GET','POST'])
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
                conn.close_cursor_and_connection()
                return make_response({'success':course_list},200)  
            else:
                errors = {
                    'errors': form_errors(form)
                }
                conn.close_cursor_and_connection()
                return make_response(errors,422)                
    

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
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to retrieve student information'},503)
    
@app.route('course/calendarEvents',methods=['GET','POST'])
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
                conn.close_cursor_and_connection()
                
                return make_response({'success':events},200)
            else:
                errors = {
                    'errors': form_errors(form)
                }
                conn.close_cursor_and_connection()
                return make_response(errors,422)

        
        

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
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to retreive calendar Events'},503)
    


@app.route('course/calendarEvents/<studentID>',methods=['GET','POST'])
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
                conn.close_cursor_and_connection()                
                return make_response({'success':events},200)

            
            else:
                errors = {
                    'errors': form_errors(form)
                }
                conn.close_cursor_and_connection()
                return make_response(errors,422)
            
        
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
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to retreive calendar Events'},503)
    


@app.route('/course/calendarEvents/create/<courseID>',methods=['GET','POST'])
def createCalendarEvent(courseID):
    form  = createCalendarEvent()

    try:
        conn = connectionHandler()

        '''For the implementation here for the front when the option is selected to 
            Add a calendar event the couse ID is passed as a hidden field so once the form 
            is resubmitted that course ID can be used to insert in CalEventOfCourse table
            - R.Senior
            '''

        if request.method == 'POST':
            if form.validate():

                eDate  = form.eventDate.data
                eTime = form.eventTime.data
                eName = form.eventName.data
                eContent = form.eventContent.data
                cID = form.courseID.data



                sql_stmt = "INSERT INTO CalendarEvents(calEvName, calEventContents,evDate,evTime) VALUES(%(name)s,%(content)s,%(date)s,%(time)s);"
                conn.cursor.execute(sql_stmt,{'name':eName,'content':eContent,'date':eDate,'time':eTime})
                conn.cursor.commit()


                sql_stmt_getID = "SELECT calEvNo FROM CalendarEvents WHERE calEvName = %()s AND calEventContents = %()s AND evDate = %()s AND  evTime = %()s;"
                conn.cursor.execute(sql_stmt_getID,{'name':eName,'content':eContent,'date':eDate,'time':eTime})

                id = conn.cursor.fetchone()

                sql_stmt_CalCourse = "INSERT INTO CalEventOfCourse((calEvNo, cID) VALUES (%(id)s, %(courseID)s);"
                conn.cursor.execute(sql_stmt_CalCourse,{'id':id,'courseID':cID})
                conn.cursor.commit()
                conn.close_cursor_and_connection()
                

        """Need to figure out a way to retrieve the course ID in order to write to the table CalEventOfCourse from a API request 
        and Not just the front end"""

                
    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()

        return make_response({'error':'An error occurred when attempting to create the calendar Event'},503)
    
    if request.method == 'GET':
        pass
        """The form upon the get request should have the following set BEFORE being passed to render template
        form.courseID.data = courseID
        -R.Senior
        """
    """return the rendered template of the empty form"""

@app.route('/course/forums/<courseID>',methods=['GET'])
def getForums(courseID):
    
    try:
        conn = connectionHandler()

        sql_stmt = "SELECT * FROM DiscussionForum WHERE forumNo in (SELECT forumNo FROM DiscussionForum WHERE cID = %(cid)s);"

        conn.cursor.execute(sql_stmt,{'cid':courseID})

        discuss_List= []

        if not conn.close_cursor:
             conn.close_cursor_and_connection()
             return make_response({'Info': []},204)

        for forumNo, forumTitle, forumMessage in conn.cursor:
            discussion ={}
            discussion['forumNo'] =  forumNo
            discussion['forumTitle'] = forumTitle
            discussion['forumMessage'] = forumMessage
            discuss_List.append(discussion)
        conn.close_cursor_and_connection()
        return make_response({'suceess':discuss_List},200)

    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to retreive forums'},503)

@app.route('/course/forum/create/<courseID>',methods=['GET','POST'])
def createForum(courseID):
    form = DiscussionForum()

    try: 
        conn = connectionHandler()

        if request.method == 'POST':
            if form.validate():
                title = form.ForumTitle
                msg = form.ForumMsg

                sql_stmt = "INSERT INTO DiscussionForumContent( forumTitle, forumMessage) VALUES(%(t)s, %(m)s);"
                conn.cursor.execute(sql_stmt,{'t':title,'m':msg})
                conn.cursor.commit()
            else:
                errors = {
                    'errors': form_errors(form)
                }
                conn.close_cursor_and_connection()
                return make_response(errors,422)
            
            sql_stmt_getID = "SELECT forumNo FROM DiscussionForumContent WHERE forumTitle = %(forumTitle)s AND forumMessage = %(forumMessage)s;"
            conn.cursor.execute(sql_stmt_getID,{'forumTitle':title,'forumMessage':msg})
            id = conn.cursor.fetchone()
            sql_stmt_CalCourse = "INSERT INTO DiscussionForum((forumNo, cID) VALUES (%(id)s, %(courseID)s);"
            conn.cursor.execute(sql_stmt_CalCourse,{'id':id,'courseID':courseID})
            conn.cursor.commit()
            conn.close_cursor_and_connection()

        
        if request.method == 'GET':
            pass
            conn.close_cursor_and_connection()            
            """Return templaate and form"""


    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to retreive forums'},503)

@app.route('course/forum/thread/<forumID>',methods=['GET'])
def getDiscussionThread(forumID):

    try:
        conn = connectionHandler()
        sql_stmt = "SELECT * FROM DiscussionThreadContent WHERE threadNo IN(SELECT threadaNo FROM DiscussionThread WHERE forumNo = %(fNo)s);"
        conn.cursor.execute(sql_stmt,{'fNo':forumID})

        threads = []
        for  threadTitle, threadMessage in conn.cursor:
            thread = {}
            thread['title']= threadTitle
            thread['message'] = threadMessage
            threads.append(thread)

        conn.close_cursor_and_connection()
        return make_response({'success':threads},200)
    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to retreive forums'},503)
    

@app.route('course/forum/thread/create/<forumNo>',methods=['GET','POST'])
def createThread(forumNo):
    
    form = DiscussionForum()

    try:
        if request.method == 'POST':
            if form.validate():
                
                msg = form.ForumMsg.data
                title = form.ForumTitle.data
                conn = connectionHandler()
                sql_stmt  = "INSERT INTO DiscussionThreadContent(threadTitle, threadMessage) VALUES(%(tt)s,%(tm)s);" 
                conn.cursor.execute(sql_stmt,{'tt':title, 'tm':msg})
                conn.cursor.commit()

                sql_stmt_getID = "SELECT threadNo FROM DiscussionThreadContent WHERE threadTitle = %(tt)s AND threadMessage = %(tm)s;"
                conn.cursor.execute(sql_stmt_getID,{'tt':title, 'tm':msg})
                id = conn.cursor.fetchone()

                sql_stmt_insert = "INSERT INTO DiscussionThread(forumNo, threadNo) VALUES(%(fNo)s, %(tNo)s);"
                conn.cursor.execute(sql_stmt_insert,{'fNo':forumNo,'tNo':id})
                conn.cursor.commit()
                
                conn.close_cursor_and_connection()

            else:
                errors = {
                    'errors': form_errors(form)
                }
                conn.close_cursor_and_connection()
                return make_response(errors,422)

        if request.method == 'GET':
            pass
            """return the render template along with the form"""    

        
    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to create a thread'},503)


@app.route('/course/content/<coruseID>',methods=['GET'])
def getCourseContent(courseID):
    
    try:
        conn = connectionHandler()
        sql_stmt = "SELECT * FROM SectionItem WHERE secItemNo IN (SELECT secItemNo FROM SectItemOfSection WHERE secNo IN (SELECT secNo FROM SecOfCourse WHERE cID = %(cID)s));"
        conn.cursor.execute(sql_stmt,{'cID':courseID})

        contents  =[]

        if not conn.cursor:
            conn.close_cursor_and_connection()
            return make_response({'Info': []},204)            

        for conName, conType, conDec in conn.cursor:
            content = {}
            content['name'] = conName
            content['conType'] = conType
            content['conDec'] = conDec

            contents.append(content)
        
        conn.close_cursor_and_connection()
        return make_response({'success':contents},200)

    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to get course content'},503)


@app.route('/course/section/<courseID>/<sectionID>',methods=["GET"])
def getSectionContent(courseID,sectionID):
    try:
        conn = connectionHandler()
        """The query below is partially completed as is the for loop below it.
            As it is now it returns the list of section items it needs to return the list of all the 
            DIFFERENT types of section Items
            -R. Senior
            """
        sql_stmt = "SELECT * FROM SectionItem WHERE secItemNo IN (SELECT secItemNo FROM SectItemOfSection WHERE secNo = %(sINo)s IN (SELECT secNo FROM SecOfCourse WHERE cID = %(cID)s));"
        conn.cursor.execute(sql_stmt,{'sINo':sectionID,'cID':courseID})
        secContent = []
        
        if not conn.cursor:
            conn.close_cursor_and_connection()
            return make_response({'Info': []},204)               
        
        for conName, conType, conDec in conn.cursor:
            content = {}
            content['name'] = conName
            content['conType'] = conType
            content['conDec'] = conDec

            secContent.append(content)
            
        conn.close_cursor_and_connection()
        return make_response({'success':secContent},200)
        

    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to get course sections'},503)


@app.route('/course/section/add/<courseID>',methods=['GET','POST'])
def addSection(courseID):
    try:
        conn = connectionHandler()
        form = createSection()

        if request.method == 'POST':
            if form.validate():
                name = form.name.data
                cID = form.courseID.data

                sql_stmt = "INSERT INTO Section(secNmae) VALUES(%(sn)s);"
                conn.cursor.execute(sql_stmt,{'sn':name})
                conn.cursor.commit()

                sql_stmt_id = "SELECT secid FROM Section WHERE secName = %(sn)s;"
                conn.cursor.execute(sql_stmt_id,{'sn':name})

                id = conn.cursor.fetchone()

                sql_stmt_insert = "INSERT INTO SecOfCourse(secNo, cID) VALUES(%(id)s,%(cID)s)"
                conn.cursor.execute(sql_stmt_insert,{'id':id,'cID':cID})
                conn.cursor.commit()

                conn.close_cursor_and_connection()
                return make_response({'success':'Section created'},200)
            
        if request.method == 'GET':
            form.courseID.data = courseID

            """return rendered template with form"""
        else:
                errors = {
                    'errors': form_errors(form)
                }
                conn.close_cursor_and_connection()
                return make_response(errors,422)     

        if request.method == 'GET':
            form.courseID.data = courseID
            pass

    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to add course section'},503)

    

@app.route('/course/section/content/add',methods=['GET','POST'])
def addContent():
    pass

@app.route('/course/assignment',method=['GET'])
def getAssignments():
    pass

@app.route('/course/assignment/submit',methods = ['GET','POST'])
def submitAssignment():
    pass

@app.route('/course/assignment/grade',methods = ['GET','POST'])
def gradeAssignment():
    pass


@app.route('course/report', method =['GET'])
def repot():
    pass




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
