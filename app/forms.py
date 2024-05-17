from wtforms import widgets, StringField, SubmitField, TextAreaField, PasswordField, BooleanField, SelectField, SelectMultipleField, ValidationError
from wtforms.validators import DataRequired, Length, regexp, EqualTo, Email
from flask_wtf import FlaskForm
from app.models import User

def validate_min_tags(form, field):
    if len(field.data) < 1:
        raise ValidationError('At least one tag must be selected.')

def validate_max_tags(form, field):
    if len(field.data) > 6:
        raise ValidationError('No more than 6 tags can be selected.')
    
def validate_user_exist(form, field):
    user = User.query.filter_by(username = field.data).first()
    if user:
        raise ValidationError('The username already exists')
    
def validate_email_exist(form, field):
    user = User.query.filter_by(email = field.data).first()
    if user:
        raise ValidationError('The username already exists')
    
def validate_email_or_user(form, field):
    if len(field.data.split('@')) == 2:
        user_email = User.query.filter_by(email = field.data).first()
        if not user_email:
            raise ValidationError("Email doesn't exist")
    else:
        user_name = User.query.filter_by(username = field.data).first()
        if not user_name:
            raise ValidationError("Username doesn't exist")
    
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

class QuestionForm(FlaskForm):
    title = StringField('Question', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Post')
    tags = MultiCheckboxField('Tags', validators=[DataRequired(), validate_min_tags, validate_max_tags])

    def set_choices(self, choices):
        self.tags.choices = [(choice, choice) for choice in choices]
    
class LoginForm(FlaskForm):
    username_email = StringField('Username or Email', validators=[DataRequired(), validate_email_or_user])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), validate_user_exist, Length(min=4, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email(), validate_email_exist])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class AnswerForm(FlaskForm):
    answer = TextAreaField('Answer', validators=[DataRequired()])
    submit = SubmitField('Post')
