from pony.orm import *
from pony import orm
from users import def_users_entity

db = Database()
db.bind(provider='sqlite', filename='pony_test.db', create_db=True)
def_users_entity(db, orm)
db.generate_mapping(create_tables=True)


# sql_debug(True)
# db.drop_table('users')
# db.generate_mapping(create_tables=True, check_tables=True)