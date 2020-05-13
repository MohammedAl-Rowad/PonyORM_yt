from pony.orm import *
from pony import orm
from users import def_users_entity
from posts import def_posts_entity

db = Database()
db.bind(provider='sqlite', filename='pony_test.db', create_db=True)
users_class = def_users_entity(db, orm)
def_posts_entity(db, orm, users_class)
db.generate_mapping(create_tables=True)


# sql_debug(True)
# db.drop_table('users')
# db.generate_mapping(create_tables=True, check_tables=True)