from flask import Flask, render_template, redirect
from sqlalchemy.orm.collections import collection

from data import db_session
from data.jobs import Jobs
from data.news import News
from data.users import User
from forms.loginform import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def init_data_users():
    session = db_session.create_session()
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.set_password("cap")

    user1 = User(
        surname="Las",
        name="Parker",
        age=23,
        position="medic",
        speciality="research engineer",
        address="module_1",
        email="las@mars.org")
    user1.set_password("123")

    user2 = User(
        surname="Sco",
        name="Dley",
        age=21,
        position="rid",
        speciality="research engineer",
        address="module_1",
        email="ssssf@mars.org")
    user2.set_password("123")

    user3 = User(
        surname="Scott",
        name="Ridley",
        age=21,
        position="captain",
        speciality="research engineer",
        address="module_1",
        email="sc@mars.org")
    user3.set_password("123")

    session.add(user)
    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.commit()


def init_data_jobs():
    db_sess = db_session.create_session()
    # user = db_sess.query(User).filter(User.id == 1).first()
    job1 = Jobs(team_leader=1, job='deployment of residential modules 1 and 2',
                work_size=15, is_finished=False, collaborators='1, 2')
    job2 = Jobs(team_leader=2, job=' of residential modules 1 and 2',
                work_size=15, is_finished=False, collaborators='1, 2')
    job3 = Jobs(team_leader=3, job='sincist',
                work_size=15, is_finished=False, collaborators='3, 2')
    job4 = Jobs(team_leader=4, job='deployment of work',
                work_size=15, is_finished=True, collaborators='4, 2')

    db_sess.add(job1)
    db_sess.add(job2)
    db_sess.add(job3)
    db_sess.add(job4)
    db_sess.commit()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
        )
        user.set_password("123")
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)

def main():
    db_session.global_init("db/mars_explorer.db")
    # init_data_users()
    # init_data_jobs()
    app.run()


if __name__ == '__main__':
    main()
