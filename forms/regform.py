from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = StringField('логин', validators=[DataRequired()])
    password = PasswordField('пароль', validators=[DataRequired()])
    password_again = PasswordField('повторите пароль', validators=[DataRequired()])
    name = StringField('имя', validators=[DataRequired()])
    surname = StringField('фамилия', validators=[DataRequired()])
    position = StringField('должность', validators=[DataRequired()])
    speciality = StringField('профессия', validators=[DataRequired()])
    age = StringField('возраст', validators=[DataRequired()])
    address = StringField('адрес', validators=[DataRequired()])

    submit = SubmitField('Зарегистрироваться')