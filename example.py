from flask import Flask, render_template, redirect
from data import db_session
from data.db_session import global_init, create_session
from data.jobs import Jobs
from data.user import User
from data.users import User
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db = input()
global_init(db)
db_sess = create_session()

res = db_sess.query(User.filter(User.address == 'module_1',
                                User.positionUser.notlike('%Иван%'),
                                User.positionUser.notlike('%Иван%'))).all()
for users in res:
    print(users.id)
