from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, DateField,TimeField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired, Email,DataRequired


'''
the validator Length(min=MIN, max=MAX)
should be added to the respected entities. in order for this to be done
the DB needs to be created. The created DB will have the required constraints for
the max values for the fields. This ensures that data validation and integrity 
starts from the the front end. 
-R. Senior
'''


class Registration(FlaskForm):
    Fname  = StringField('FirstName', validators=[InputRequired()])
    mName = StringField('MiddleName',validators=[InputRequired()])
    Lname = StringField('LastName', validators=[InputRequired()])
    Passowrd = PasswordField('Password',validators=[InputRequired()])

class StudentRegistration(Registration):
    StudentID = StringField('studentID',validators=[InputRequired()])


'''My Understanding of it is that an adminstrator will have the duty 
    of verifying the account of an employee. this will be accomplished by using the 
    is_active(https://flask-login.readthedocs.io/en/latest/) attr of the user 
    account from the Flask_login library.
    -R.Senior'''

class LecturerRegistration(Registration):
    LectureID = StringField('LecturerID',validators=[InputRequired()])


class AdminRegistration(Registration):
    AdminID  = StringField('AdminID',validators=[InputRequired()])

class CourseMantainerRegistration(Registration):
    CourseMaintainerID  = StringField('CourseMaintainerID',validators=[InputRequired()])



class Login(FlaskForm):
    userID = StringField('UID',validators=[InputRequired()])
    Password = PasswordField('Password',validators=[InputRequired()])


class CreateCourse(FlaskForm):
    CourseName = StringField('cName',validators=[InputRequired()])
    CourseCode = StringField('cCode',validators=[InputRequired()])
    # cID assigned by DB

class AssignLecturerToCourse(FlaskForm):

    # validate choices set to true means selection must come from the predefined list
    #there are exceptions in using valid choices https://wtforms.readthedocs.io/en/2.3.x/fields/ under SelectField subheading

    LecturerOptions = SelectField('Lecturer',validate_choice=True)
    CourseOptions = SelectField('Course',validate_choice=True)

class CourseRegistration(FlaskForm):
    # validate choices set to true means selection must come from the predefined list
    #there are exceptions in using valid choices https://wtforms.readthedocs.io/en/2.3.x/fields/ under SelectField subheading
    StudentID = StringField('studentID',validators=[InputRequired()])
    CourseOptions = SelectField('Course',validate_choice=True)

class GetRegisteredStudents(FlaskForm):
    CourseOptions = SelectField('Course',validate_choice=True)

class GetCalendarEvents(FlaskForm):
    CourseOptions = SelectField('Course',validate_choice=True)

class getStudentCalendarEvents(FlaskForm):
    student = StringField('studentID',validators=[InputRequired()])
    CourseOptions = SelectField('Course',validate_choice=True)


class createCalendarEvent(FlaskForm):
    eventDate= DateField('EventDate',validators=[InputRequired()])
    eventTime = TimeField('EventTime',validators=[InputRequired()])
    eventName = StringField('EventName',validators=[InputRequired()])
    eventContent = StringField('EventContent') # This field is not made mandatory 

    # the following may help to hide the cID on the front end https://stackoverflow.com/questions/27071284/hiding-a-form-group-with-flask-jinja2-and-wtforms
    courseID = StringField('cID',validators=[InputRequired()]) # this field should be hidden to the user
        #calEvNo Assigned by DB
    
    
class DiscussionForum(FlaskForm):
    # Discussion forum ID (forumNo) assigned by DB
    #cID assigned by the hidden field in version2 of the API
    ForumTitle = StringField('ForumTitle',validators=[InputRequired()])
    ForumMsg = StringField('ForumMsg',validators=[InputRequired()])




class DiscussionThread(FlaskForm):
    #dtID assigned by DB
    #dfID assigned by API
    title = StringField('ThrdName',validators=[InputRequired()])
    Post = StringField('PostName',validators=[InputRequired()])


    

