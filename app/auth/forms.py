from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, SubmitField, BooleanField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from ..models import User 


class SignupForm(FlaskForm):
    username = StringField('Please enter your username...', validators=[Required()])
    email = StringField('Please enter your email address...',validators=[Required(),email()])
    password = PasswordField('Please enter your password...',validators=[Required(),EqualTo('password_check',message='Please ensure passwords match')])
    password_check = PasswordField('Enter your password again...',validators=[Required()])
    submit = SubmitField('Confirm')


    def check_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('Email address already taken')

    
    def check_name(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Sorry the username you chose seems to be taken already')



class LoginForm(FlaskForm):
    
    email = StringField('Your email address...',validators=[Required(),email()])
    password = PasswordField('Your password...',validators=[Required()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')