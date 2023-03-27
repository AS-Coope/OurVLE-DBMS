from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired, Email


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
    # cID assigned by DB

class DiscussionForum(FlaskForm):
    # dfID assigned by DB
    #cID assigned by the API
    ForumName = StringField('ForumName',validators=[InputRequired()])

class DiscussionThread(FlaskForm):
    #dtID assigned by DB
    #dfID assigned by API
    title = StringField('ThName',validators=[InputRequired()])
    Post = StringField('PostName',validators=[InputRequired()])
    
