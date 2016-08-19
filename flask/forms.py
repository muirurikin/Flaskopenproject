from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Regexp, ValidationError,Email, Length, EqualTo

# create a registration form
class RegisterForm(Form):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-z0-9_]+',
                message='User name should be one word,letters, numbers and underscores only'
            )
        ])
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()


        ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo('password2', 'Passwords must match')
        ])
    password2 = PasswordField(
        'Confirm Password',
        validators=[DataRequired()]
    )


# create a login form
class LoginForm(Form):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


# create a post form
class PostForm(Form):
    content = TextAreaField("Post anything!", validators=[DataRequired()])