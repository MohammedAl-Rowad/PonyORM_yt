from pony.orm import db_session
from faker import Faker
fake = Faker()

@db_session()
def fake_users(orm, Users, amount = 10):
    for _ in range(amount):
        u = Users(
            first_name=fake.first_name(), 
            second_name=fake.last_name(),
            age=fake.random_int(18, 99),
            email=fake.ascii_free_email(),
            )


@db_session()
def del_user(Users, id):
    u = Users.select(lambda user: user.id == id)
    u.delete()

@db_session()
def delete_users_bulk(Users):
    Users.select(lambda u: 'gmail' in u.email or 'hotmail' in u.email).delete(bulk=True)

@db_session()
def update_user(Users, id, name):
    Users[id].first_name = name
