
from flask import Flask, render_template, request, make_response,jsonify,session
from pprint import pprint
# from flask_login import current_user , login_user,login_required, logout_user
# from werkzeug.security import check_password_hash
from passlib.hash import sha256_crypt
import mysql.connector
import base64

from dotenv import load_dotenv
load_dotenv()

import os
# from app.forms_OurVLE import *



"""
snippet here
password = sha256_crypt.hash("password")
password2 = sha256_crypt.hash("password")

print(password)
print(password2)

print(sha256_crypt.verify("password", password))
"""






USER =  os.environ.get('USER')
PASSWORD =  os.environ.get('PASSWORD')
HOST = os.environ.get('HOST')
DATABASE =  os.environ.get('DATABASE')


class connectionHandler:

    def __init__(self) -> None:
        self.connection = self.make_connection_cursor()
        self.cursor =  self.connection.cursor(buffered=True)

    @classmethod
    def make_connection_cursor(self):
        return mysql.connector.connect(user=USER, password=PASSWORD,
                                host=HOST,
                                database=DATABASE)
    
    def setbufferFalse(self):
         self.cursor(buffered = False)

    def setbufferTrue(self):
         self.cursor(buffered = True)
    
    def close_cursor(self):
        self.cursor.close()
    
    def close_connection(self):
        self.connection.close()
    
    def close_cursor_and_connection(self):
        self.cursor.close()
        self.connection.close()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """This displays the index page for OurVLE it shows the courses 
        to the guess user
    """
    return render_template('base.html')




        
@app.route('/registration/employee-registration',methods=[ 'POST'])
def empRegister():

    LecturerRegistration = request.json
    
    fName = LecturerRegistration['fName']
    mName = LecturerRegistration['mName']
    lName = LecturerRegistration['lName']
    LectID = LecturerRegistration['LectID']
    pwd = LecturerRegistration['pwd']
    acNo = 'LEC' + LectID
    dept = LecturerRegistration['DeptID']
    email = LecturerRegistration['email']
    
    hashedPassword = sha256_crypt.hash(pwd)
    try:
        conn = connectionHandler()



        sql_stmt = "INSERT into LECTURER (lID,Password,email) VALUES( %(lectID)s, %(lectpwd)s, %(email)s);"  # Used to secure SQL statements to prevent injection
        conn.cursor.execute(sql_stmt,{'lectID':LectID,'lectpwd':hashedPassword, 'email':email})

        sql_2 = "INSERT into LecturerAccount(lID,acNo) VALUES(%(lectID)s, %(n)s);"
        conn.cursor.execute(sql_2,{'lectID':LectID, 'n':acNo})

        sql_3 = "INSERT into lectofdept(lID, deptID) VALUES(%(l)s, %(d)s);"
        conn.cursor.execute(sql_3,{'l':LectID, 'd':dept})

        sql_4 = "INSERT into lectname(lID,lfName,lmName,llName) VALUES(%(LID)s,%(f)s,%(m)s,%(l)s);"
        conn.cursor.execute(sql_4,{'LID':LectID,'f':fName,'m':mName,'l':lName})

        conn.connection.commit()

        conn.close_cursor_and_connection()
        return make_response({'success':'Your account has been created.'},201)
    
    except mysql.connector.Error as err:
        conn.close_cursor_and_connection()
        return make_response({'error': f"The following error occured: {err}"},500)
    except Exception as ex:
        conn.close_cursor_and_connection()
        return make_response({'error': "There has been an error in communicating with the database when attempting to creating your account. Please contact your system administrator"}, 503)
    
    

        

@app.route('/registration/student-registration',methods=['POST'])
def studentRegister():
        student = request.json
        fName = student['fName']
        mName = student['mName']
        lName = student['lName']
        stuID = student['stuID']
        pwd =   student['pwd']
        email = student['email']
        dept = student['deptID']
        hashedPassword = sha256_crypt.hash(pwd)
   
        try:
            conn = connectionHandler()
            sql_stmt = "INSERT into Student (studID,Password,email) VALUES( %(sID)s, %(spwd)s, %(mail)s);"  # Used to secure SQL statements to prevent injection
            conn.cursor.execute(sql_stmt,{'sID':stuID,'spwd':hashedPassword, 'mail':email})

            
            sql_3 = "INSERT into StudentName(studID, sfName, smName, slName) VALUES(%(sID)s, %(fn)s, %(mn)s, %(ln)s);"
            conn.cursor.execute(sql_3,{'sID':stuID, 'fn':fName, 'mn':mName, 'ln':lName})
            
            sql_4 = "INSERT into StudentOfDept(studID, deptID) VALUES(%(s)s, %(d)s);"
            conn.cursor.execute(sql_4,{'s':stuID,'d':dept})

            conn.connection.commit()
            conn.close_cursor_and_connection()
            return make_response({'success':'Your account has been created.'},201)
        except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
        
        except Exception as ex:
            return make_response({'error': "There has been an error in communicating with the database when attempting to create your account. Please contact your system administrator"}, 503)
    


"""_summary_
    Creates a Course
Returns:
    Unauthorised: Informs the user that they do not have the prvilage to access the requested content
    Success: Informs the user that a particular course has been created
    error: Appropriate error message
"""

@app.route('/course/create',methods=['POST'])
def createCourse():

    course = request.json   
    cID = course['cID'].strip()
    cfName = course['cfName'].strip()
    lID  = course['lID'].strip()
    deptID =  course['deptID'].strip()
    try:
        conn = connectionHandler()
        sql_stmt = "INSERT into Course (cID,cfName) VALUES(%(cID)s, %(cn)s);"        
        conn.cursor.execute(sql_stmt,{'cID':cID,'cn':cfName})

        sql_2 = "INSERT into LectOfCourse(cID, lID) VALUES(%(c)s,%(l)s);"
        conn.cursor.execute(sql_2,{'c':cID,'l':lID})

        sql_3 = "INSERT into CourseInDept(cID, deptID) VALUES(%(c)s,%(d)s);"
        conn.cursor.execute(sql_3,{'c':cID,'d':deptID})
        
        conn.connection.commit()
        conn.close_cursor_and_connection()
        return make_response({'success':f'The course, {cfName} has been created.'},201)
    

    except mysql.connector.Error as err:
        conn.close_cursor_and_connection()
        return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        return make_response({'error': f"There has been an error in communicating with the database when attempting to creat the course {cTitle}. Please contact your system administrator"}, 503)
    


"""_summary_
    Retrieve all the courses
Returns:
    Success: list of courses ad dictionary objects
    Error: Appropriate error message
"""
@app.route('/courses/',methods=['GET'])
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
    

    
@app.route('/courses/student/<studentId>',methods=['GET'])
def getStudentCourse(studentId):

    studentId = studentId.strip()
    try:
        conn = connectionHandler()

        ''''To complete this query it should search in the enrollment table for the student ID
            then with the cIDs that it have -if any- search for the course titles'''
        
        sql_stmt = "SELECT DISTINCT cID FROM courseofStud WHERE studID  =%(sID)s;" # select cIDs for student
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


@app.route('/courses/lecturer/<lectID>',methods=['GET'])
def lecturerCourses(lectID):
    lectID = lectID.strip()
    try:
        conn = connectionHandler()

        ''''To complete this query it should search in the LectOfCourse table for the lect ID
            then with the lectID that it have -if any- search for the course titles'''
        
        sql_stmt = "SELECT DISTINCT cID FROM  lectofcourse WHERE lID  =%(lectID)s;" # select cIDs for Lecturer
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


@app.route('/course/assign',methods=['POST'])
def assignLecturer():
    
    try:
        conn = connectionHandler()

        LecturerOptions = request.json
        lectID = LecturerOptions['lectID'].strip()
        courseID = LecturerOptions['courseID'].strip()
        sql_stmt = "SELECT COUNT(lID) FROM LectOfCourse WHERE cID  =%(courseID)s;"
        conn.cursor.execute(sql_stmt,{'courseID':courseID})
        count = conn.cursor.fetchone()[0]
        print(count)

        sql_2 = "SELECT COUNT(cid) FROM LectOfCourse WHERE lID  = %(l)s;"
        conn.cursor.execute(sql_2,{'l':lectID})
        count2 = conn.cursor.fetchone()[0]
        print(count2)
        if int(count2) > 4:
            conn.close_cursor_and_connection()
            return make_response({'error':'This lecturer is already doing max amount of courses.'},303)
            
        else:
            sql_insert_stmt = "INSERT INTO LectOfCourse(cID,lID) VALUES(%(cid)s, %(lectID)s);"
            conn.cursor.execute(sql_insert_stmt,{'cid':courseID,'lid':lectID})
            conn.connection.commit()
            conn.close_cursor_and_connection()
            return make_response({'success':f'The course has been assigned a lecturer'},201)


    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to update the course information'},503)



@app.route('/course/registration',methods=['POST'])
def courseRegistration():

    try:
        conn = connectionHandler()

        CourseRegistration = request.json

        studentID = CourseRegistration['studentID'].strip()
        courseID = CourseRegistration['courseID'].strip()

        #check if the student is already registered
        sql_stmt_check_if_alrady_reg = "select IF((SELECT COUNT(studID) FROM courseofStud WHERE cID = %(courseID)s AND studID = %(studentID)s) > 0, 'Yes', 'No') as Result;"
        conn.cursor.execute(sql_stmt_check_if_alrady_reg,{'courseID':courseID,'studentID':studentID})
        resp1 = conn.cursor.fetchone()[0]
        print(resp1)
        
        if resp1 == 'Yes':
            return make_response({'error': "the Student is already registerd for the selected course"},400)
        
        #check to ensure the student is registered in no more that 6 courses
        sql_stmt_check_course_limit = "select IF((SELECT COUNT(cID) FROM courseofStud WHERE studID = %(studentID)s) > 5, 'Yes', 'No') as Result;"
        conn.cursor.execute(sql_stmt_check_course_limit,{'studentID':studentID})

        resp2 =  conn.cursor.fetchone()[0]
        print(resp2)
        if resp2 == 'Yes':
            return make_response({'error': "the student is already registered for the maximum of 6 credits"},400)
        
        #if all requirements are met commit
        sql_stmt_register = "INSERT INTO courseofStud (studID,cID) VALUES(%(stuID)s, %(crsID)s);"
        conn.cursor.execute(sql_stmt_register,{'stuID':studentID,'crsID':courseID})
        conn.connection.commit()
        return make_response({'success':"The student has been registered for the course"},200)



    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to update the course information'},503)


@app.route('/course/enrollment/<courseID>',methods=['GET'])
def getRegisteredStudents(courseID):

    courseID =courseID.strip()

    try:
        conn = connectionHandler()

        sql_stmt = "SELECT DISTINCT studID FROM courseofStud WHERE cID = %(crseID)s;"
        conn.cursor.execute(sql_stmt,{'crseID':courseID})
        course_list= []
        for studID in conn.cursor:
            course_list.append(studID)
        conn.close_cursor_and_connection()
        return make_response({'success':course_list},200)              
    
    
    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to retrieve student information'},503)




@app.route('/course/calendarEvents/course/<courseID>',methods=['GET'])
def getEvents(courseID):

    courseID = courseID.strip()
    try:
        'SELECT DISTINCT cID FROM courseofStud WHERE studID  =%(sID)s;'
        conn = connectionHandler()
        """The Add query to acess CalendarEvents and CalEventOfCourse"""
        sql_stmt = "SELECT * FROM calendarevents WHERE calEvNo IN (SELECT CalEvNo FROM CalEventOfCourse WHERE cID = %(cid)s);"
        conn.cursor.execute(sql_stmt,{'cid':courseID})
        events= []
        for calevno,calEvName,calEventContents,evDate,evTime in conn.cursor:
            event ={}
            event['evDate']  = evDate
            event['calEventContents'] = calEventContents        
            event['evTime'] = str(evTime)
            event['calEvName'] = calEvName
            
            events.append(event)
        conn.close_cursor_and_connection()
        
        return make_response({'success':events},200)

    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to retreive calendar Events'},503)
    


@app.route('/course/calendarEvents/student/<studentID>',methods=['GET'])
def getStudentEvents(studentID):
    studentID = studentID.strip()
    try:
        conn = connectionHandler()
                
        sql_stmt = "select * from calendarevents where calevNo in (select caleventofcourse.calevno from courseofstud join caleventofcourse on courseofstud.cid = caleventofcourse.cid where studid = %(studentID)s);"
        conn.cursor.execute(sql_stmt,{'studentID':studentID})
        events= []
        for calevno,calEvName,calEventContents,evDate,evTime in conn.cursor:
            event ={}
            event['evDate']  = evDate
            event['calEventContents'] = calEventContents        
            event['evTime'] = str(evTime)
            event['calEvName'] = calEvName
            
            events.append(event)
        conn.close_cursor_and_connection()                
        return make_response({'success':events},200)

    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()

        return make_response({'error':'An error occurred when attempting to retreive calendar Events for the student.'},503)
    


@app.route('/course/calendarEvents/create/',methods=['POST'])
def createCalendarEvent():
    createCalendarEvent = request.json

    try:
        conn = connectionHandler()

        eDate  = createCalendarEvent['eDate'] 
        eTime = createCalendarEvent['eTime'] 
        calevName = createCalendarEvent['calevName'] 
        eContent = createCalendarEvent['eContent'] 
        cID = createCalendarEvent['cID'] 

        sql_stmt = "INSERT INTO CalendarEvents(calEvName, calEventContents,evDate,evTime) VALUES(%(name)s,%(content)s,%(date)s,%(time)s);"
        conn.cursor.execute(sql_stmt,{'name':calevName,'content':eContent,'date':eDate,'time':eTime})
        conn.connection.commit()

        sql_stmt_getID = "SELECT calEvNo FROM CalendarEvents WHERE calEvName = %(name)s AND calEventContents = %(content)s AND evDate = %(date)s AND  evTime = %(time)s;"
        conn.cursor.execute(sql_stmt_getID,{'name':calevName,'content':eContent,'date':eDate,'time':eTime})
        id = conn.cursor.fetchone()[0]
        sql_stmt_CalCourse = "INSERT INTO CalEventOfCourse(calEvNo, cID) VALUES (%(id)s, %(courseID)s);"
        conn.cursor.execute(sql_stmt_CalCourse,{'id':id,'courseID':cID})
        conn.connection.commit()
        conn.close_cursor_and_connection()
        return make_response({'success':f'The Event, {calevName} has been created'},200)
                             
    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()

        return make_response({'error':'An error occurred when attempting to create the calendar Event'},503)




@app.route('/course/forums/<courseID>',methods=['GET'])
def getForums(courseID):
    
    courseID =courseID.strip()
    try:
        conn = connectionHandler()

        sql_stmt = "SELECT * FROM DiscussionForumContent WHERE forumNo in (SELECT forumNo FROM DiscussionForum WHERE cID = %(cid)s);"

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





@app.route('/course/forum/create/',methods=['POST'])
def createForum():
    DiscussionForum = request.json

    try: 
        conn = connectionHandler()
            
        title = DiscussionForum['title'].strip() 
        msg = DiscussionForum['msg'].strip()
        courseID = DiscussionForum['courseID'].strip()
        
        
        sql_stmt = "INSERT INTO DiscussionForumContent( forumTitle, forumMessage) VALUES(%(t)s, %(m)s);"
        conn.cursor.execute(sql_stmt,{'t':title,'m':msg})
        conn.connection.commit()
         
        sql_stmt_getID = "SELECT forumNo FROM DiscussionForumContent WHERE forumTitle = %(forumTitle)s AND forumMessage = %(forumMessage)s;"
        conn.cursor.execute(sql_stmt_getID,{'forumTitle':title,'forumMessage':msg})
        id = conn.cursor.fetchone()[0]


        sql_stmt_check_if_alrady_in = "select IF((SELECT COUNT(forumNo) FROM discussionforum WHERE forumNo = %(fno)s ) > 0, 'Yes', 'No') as Result;"
        conn.cursor.execute(sql_stmt_check_if_alrady_in,{'fno':id})
        resp1 = conn.cursor.fetchone()[0]

        if resp1 == 'Yes':
            
            return make_response({'error': "the Forum Already exists."},400)
        

        sql_stmt_CalCourse = "INSERT INTO DiscussionForum(forumNo,cid) VALUES (%(fid)s,%(courseID)s);"
        conn.cursor.execute(sql_stmt_CalCourse,{'fid':id,'courseID':courseID})
        conn.connection.commit()
        
        conn.close_cursor_and_connection()
        return make_response({'suceess':'The Forum has been created!'},200)        


    except mysql.connector.Error as err:
            
            
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        

        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to retreive forums'},503)

@app.route('/course/forum/thread/<forumID>',methods=['GET'])
def getDiscussionThread(forumID):
    forumID =forumID.strip()
    try:
        conn = connectionHandler()
        sql_stmt = "SELECT * FROM DiscussionThreadContent WHERE threadNo IN(SELECT threadNo FROM DiscussionThread WHERE forumNo = %(fNo)s);"
        conn.cursor.execute(sql_stmt,{'fNo':forumID})

        threads = []
        for  threadNo,threadTitle, threadMessage in conn.cursor:
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
    

@app.route('/course/forum/thread/create/',methods=['POST'])
def createThread():
    
    Thread = request.json
    msg = Thread['msg'].strip()
    title = Thread['title'].strip()
    forumNo = Thread['forumNo'].strip()

    try:
        conn = connectionHandler()
        sql_stmt  = "INSERT INTO DiscussionThreadContent(threadTitle, threadMessage) VALUES(%(tt)s,%(tm)s);" 
        conn.cursor.execute(sql_stmt,{'tt':title, 'tm':msg})
        conn.connection.commit()
        sql_stmt_getID = "SELECT threadNo FROM DiscussionThreadContent WHERE threadTitle = %(tt)s AND threadMessage = %(tm)s;"
        conn.cursor.execute(sql_stmt_getID,{'tt':title, 'tm':msg})
        id = conn.cursor.fetchone()
        sql_stmt_insert = "INSERT INTO DiscussionThread(forumNo, threadNo) VALUES(%(fNo)s, %(tNo)s);"
        conn.cursor.execute(sql_stmt_insert,{'fNo':forumNo,'tNo':id})
        conn.connection.commit()
        
        conn.close_cursor_and_connection()
        
    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        return make_response({'error':'An error occurred when attempting to create a thread'},503)


@app.route('/course/content/<courseID>',methods=['GET'])
def getCourseContent(courseID):
    
    try:
        conn = connectionHandler()
        sql_stmt = "select secNo from secofcourse where cid =%(cID)s;"
        conn.cursor.execute(sql_stmt,{'cID':courseID})

        contents  =[]

        if not conn.cursor:
            conn.close_cursor_and_connection()
            return make_response({'Info': []},204)            

        for secNo in conn.cursor:
            secNo = secNo[0]
            sectionContent = sectionContentHelper(secNo)
            contents.append({f'{secNo}':sectionContent})
        
        conn.close_cursor_and_connection()
        return make_response({'success':contents},200)

    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        print(ex)
        return make_response({'error':'An error occurred when attempting to get course content'},503)



@app.route('/course/section/<sectionID>',methods=["GET"])
def getSectionContent(sectionID):
    sectionContent = sectionContentHelper(sectionID)
    return make_response({'success':sectionContent},200)


@app.route('/course/section/add/',methods=['POST'])
def addSection():
    try:
        conn = connectionHandler()
        createSection = request.json
        
        name = createSection ['name']
        cID = createSection ['cID'] 
        sql_stmt = "INSERT INTO Section(secName) VALUES(%(sn)s);"
        conn.cursor.execute(sql_stmt,{'sn':name})
        conn.connection.commit()
        sql_stmt_id = "SELECT secNo FROM Section WHERE secName = %(sn)s;"
        conn.cursor.execute(sql_stmt_id,{'sn':name})
        id = conn.cursor.fetchone()[0]
        sql_stmt_insert = "INSERT INTO SecOfCourse(secNo, cID) VALUES(%(id)s,%(cID)s)"
        conn.cursor.execute(sql_stmt_insert,{'id':id,'cID':cID})
        conn.connection.commit()
        conn.close_cursor_and_connection()
        return make_response({'success':'Section created.'},200)
    

    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        #return make_response({'error':f'{ex}'},503) 
        return make_response({'error':'An error occurred when attempting to add course section'},503) 

@app.route('/course/section/content/add',methods=['POST'])
def addContent():
    addContent = request.json

    #Getting all information related to section for : sectionitem,sectionlink,sectionitemofsection cauz idk which one to add to db 
    secNo = addContent['secNo'].strip()
    conType = addContent['conType'].strip().lower() #enter whether content is link/submissionportal

    #adds sectionitem to db

    try:
        conn = connectionHandler()
        #1st check if the section exists
        sql_stmt_check_if_sec_exists = "select IF((SELECT COUNT(secNo) FROM section WHERE secNo = %(no)s) > 0, 'Yes', 'No') as Result;"
        conn.cursor.execute(sql_stmt_check_if_sec_exists,{'no':secNo})
        resp1 = conn.cursor.fetchone()[0]
     
        if resp1 == 'No':
            return make_response({'error': "The section that you wish to add to does not exist."},400)
        
        sql_stmt1 = "INSERT INTO sectionitem(secNo) VALUES(%(sn)s);"
        conn.cursor.execute(sql_stmt1,{'sn':secNo})
        conn.connection.commit()
        
        # return the value of the last auto-incremented field that was inserted into the table.
        conn.cursor.execute("SELECT LAST_INSERT_ID();")
        secItemNo = conn.cursor.fetchone()[0]

       
        #if content is link add sectionlink to db
        if conType == "link":
            lkName = addContent['lkName']
            sql_stmt2 = "INSERT INTO link(lkName,secItemNo) VALUES(%(lkid)s, %(sn)s);"
            conn.cursor.execute(sql_stmt2,{'lkid':lkName,'sn':secItemNo})
            conn.connection.commit()
            return make_response({'success':'Link added.'},200)

        #if content is submissionportal add submissionportal to db
        if conType == "submissionportal":
            sectionItemName = addContent['sectionItemName'] #enter the name you want to be displayed for the content
            spName = sectionItemName
            dueDate = addContent['dueDate']
            sql_stmt3 = "INSERT INTO submissionportal(spName,dueDate,secItemNo) VALUES(%(spname)s, %(dd)s, %(secitem)s);"
            conn.cursor.execute(sql_stmt3,{'spname':spName, 'dd':dueDate,'secitem':secItemNo})
            conn.connection.commit()
            return make_response({'success':'Portal added.'},200)

        # if it's content
        else:
            name = addContent['name']
            secContent = addContent['secContent'] #enter the actual content eg:.pdf,.docx,image --idk how this would apply to submission portal
            sql_stmt4 = "INSERT INTO content(con_Name,secItemNo,conType,content) VALUES(%(name)s,%(sn)s,%(type)s,%(content)s);"
            conn.cursor.execute(sql_stmt4,{'name':name, 'sn': secItemNo, 'type':conType,'content':secContent})
            conn.connection.commit()
            return make_response({'success':'Content added.'},200)


    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        # return make_response({'error':f'{ex}'},503) 
        return make_response({'error':'An error occurred when attempting to add course section'},503)


@app.route('/course/assignment',methods=['GET'])
def getAssignments():
    pass

@app.route('/course/assignment/submit',methods = ['GET','POST'])
def submitAssignment():
    pass

@app.route('/course/assignment/grade',methods = ['GET','POST'])
def gradeAssignment():
    pass


@app.route('/course/report', methods =['GET'])
def report():
    pass
    #more  that 50 students
    #SELECT cName FROM Course WHERE cID IN(SELECT cID FROM CourseOfStud WHERE COUNT(cID) > 50);

    #more than 5 courses
    # SELECT sfName, smName, slName FROM StudentName WHERE studID IN(SELECT studID FROM CourseOfStud WHERE COUNT(studID) > 4);

    #All lecturers that teach 3 or more courses
    #SELECT  lfName, lmName, llName FROM LectName WHERE lID in (SELECT lID from LectOfCourse WHERE COUNT(lID) > 2);

    #The 10 most enrolled courses. 
    #SELECT cName from Course WHERE cID IN(SELECT cID FROM);



    """Helper Functions"""


def sectionContentHelper(sectionID):
    try:
        conn = connectionHandler()

        secContent = []


        # for content
        sql_stmt_content = "SELECT con_Name, conType, content FROM content WHERE  secItemNo IN(SELECT secItemNo FROM SectionItem WHERE secNo  = %(sINo)s );"            
        conn.cursor.execute(sql_stmt_content,{'sINo':sectionID})
        contentlist = []
        for con_Name,  conType, content in conn.cursor:
            content_dict = {}
            content_dict['name'] = con_Name
            content_dict['conType'] = conType
            content_blob = content
            base64_data = base64.b64encode(content_blob)
            json_data = base64_data.decode('utf-8')
            content_dict['content'] = json_data

            contentlist.append(content_dict)

        # for sub portal
        sql_stmt_submissionportal = "SELECT spName,dueDate FROM submissionportal WHERE  secItemNo IN(SELECT secItemNo FROM SectionItem WHERE secNo  = %(sINo)s );"            
        conn.cursor.execute(sql_stmt_submissionportal,{'sINo':sectionID})
        SubmissionPortal = []
        
        for spName,dueDate in conn.cursor:
            portal = {}
            portal['name'] = spName
            portal['dueDate'] = dueDate
            

            SubmissionPortal.append(portal)

        # for  Links
        sql_stmt_links = "SELECT lkName FROM link WHERE  secItemNo IN(SELECT secItemNo FROM SectionItem WHERE secNo  = %(sINo)s );"            
        conn.cursor.execute(sql_stmt_links,{'sINo':sectionID})
        linkList = []
        
        for Lkname in conn.cursor:
            link = {}
            link['linkName'] = Lkname
            

            linkList.append(link)

            
        conn.close_cursor_and_connection()
        return {'links':linkList,'SubmissionPortal':SubmissionPortal, 'content':contentlist }
        

    except mysql.connector.Error as err:
            conn.close_cursor_and_connection()
            print(err)
            # return make_response({'error': f"The following error occured: {err}"},500)
    
    except Exception as ex:
        conn.close_cursor_and_connection()
        print(ex)
        # return make_response({'error':f'{ex}'},503)
        # return make_response({'error':'An error occurred when attempting to get course sections'},503)


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


if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port=6000)