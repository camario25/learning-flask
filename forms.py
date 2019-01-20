from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators
# from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
  first_name = StringField('First name', [validators.DataRequired('Please enter your first name.')])
  last_name = StringField('Last name', [validators.DataRequired('Please enter your last name.')])
  email = StringField('Email', [validators.DataRequired('Please enter your email address.'), validators.Email('Please enter a valid email address.')])
  password = PasswordField('Password', [validators.DataRequired('Please enter your password.'), validators.Length(min=6, message='Passwords must be 6 characters or more.')])
  submit = SubmitField('Sign up')