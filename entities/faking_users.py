from pony.orm import db_session
import json
from faker import Faker
fake = Faker()

@db_session()
def fake_users(Users, Posts, amount = 10):
    for _ in range(amount):
        u = Users(
            first_name=fake.first_name(), 
            second_name=fake.last_name(),
            age=fake.random_int(18, 99),
            email=fake.ascii_free_email(),
            )
    creating_posts(Users, Posts)

@db_session()
def creating_posts(Users, Posts):
    users = Users.select()
    for user in users:
        post = Posts(title=fake.name(), body=''.join(fake.paragraphs()), user=user)

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
    
    
@db_session()
def get_users_posts(Users, Posts):
    print(
        json.dumps({'data': [p.user.to_dict() for p in Posts.select()]})
    )

