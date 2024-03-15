from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars.db")
    app.run()
    db_sess = db_session.create_session()

    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess.add(user)

    user = User()
    user.surname = 'Pushkin'
    user.name = 'Alexsandr'
    user.age = 23
    user.position = 'worker'
    user.speciality = 'writer'
    user.address = 'module_2'
    user.email = 'a_pushkin@mars.org'
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = 'Esenin'
    user.name = 'Sergey'
    user.age = 23
    user.position = 'worker'
    user.speciality = 'doctor'
    user.address = 'module_2'
    user.email = 'ser_e@mars.org'
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = 'London'
    user.name = 'Jack'
    user.age = 20
    user.position = 'worker'
    user.speciality = 'builder'
    user.address = 'module_2'
    user.email = 'londonn@mars.org'
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()
