# Import necessary modules and classes from WTForms and Flask-WTForms
from wtforms import widgets, StringField, SubmitField, TextAreaField, PasswordField, BooleanField, SelectField, SelectMultipleField, ValidationError
from wtforms.validators import DataRequired, Length, regexp, EqualTo, Email
from flask_wtf import FlaskForm
from app.models import User

# Custom validators for form fields
# User taken, email taken ect.

def validate_min_tags(form, field):
    # Ensures that at least one tag is selected
    if len(field.data) < 1:
        raise ValidationError('At least one tag must be selected.')

def validate_max_tags(form, field):
    # Restricts the number of tags that can be selected to 6 for storage and efficiency
    if len(field.data) > 6:
        raise ValidationError('No more than 6 tags can be selected.')
    
def validate_user_exist(form, field):
    # Checks if a username already exists in the database
    user = User.query.filter_by(username = field.data).first()
    if user:
        raise ValidationError('The username already exists')
    
def validate_email_exist(form, field):
    # Checks if an email already exists in the database
    user = User.query.filter_by(email = field.data).first()
    if user:
        raise ValidationError('The username already exists')
    
def validate_email_or_user(form, field):
    # Checks for the existence of a username or email in the database
    if len(field.data.split('@')) == 2:
        user_email = User.query.filter_by(email = field.data).first()
        if not user_email:
            raise ValidationError("Email doesn't exist")
    else:
        user_name = User.query.filter_by(username = field.data).first()
        if not user_name:
            raise ValidationError("Username doesn't exist")

# Custom field class for selecting multiple checkboxes from the drop downs
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

# Form classes with various fields for different functionalities

class EditProfileForm(FlaskForm):
    # Form for editing user profile
    username = StringField('Username', validators=[validate_user_exist])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    new_password = PasswordField('New Password')
    submit = SubmitField('Submit')

class QuestionForm(FlaskForm):
    # Form for posting a question
    title = StringField('Question', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Post')
    tags = MultiCheckboxField('Tags', validators=[DataRequired(), validate_min_tags, validate_max_tags])

    def set_choices(self, choices):
        # Method to set tag choices dynamically based on available tags set in controller
        self.tags.choices = [(choice, choice) for choice in choices]
    
class LoginForm(FlaskForm):
    # Form for user login
    username_email = StringField('Username or Email', validators=[DataRequired(), validate_email_or_user])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class SignupForm(FlaskForm):
    # Form for user registration
    username = StringField('Username', validators=[DataRequired(), validate_user_exist, Length(min=4, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email(), validate_email_exist])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class AnswerForm(FlaskForm):
    # Form for posting an answer to a question
    answer = TextAreaField('Answer', validators=[DataRequired()])
    submit = SubmitField('Post')
