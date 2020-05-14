from pony import orm
from users import def_users_entity
from posts import def_posts_entity
from faking_users import fake_users,del_user,delete_users_bulk,update_user

db = orm.Database()
db.bind(provider='sqlite', filename='pony_test.db', create_db=True)
users_class = def_users_entity(db, orm)
def_posts_entity(db, orm, users_class)
db.generate_mapping(create_tables=True)
fake_users(orm, users_class)
del_user(users_class, 1)
delete_users_bulk(users_class)
update_user(users_class, 3, 'rowadz')

# sql_debug(True)
# db.drop_table('users')
# db.generate_mapping(create_tables=True, check_tables=True)