from pony import orm

db = orm.Database()
db.bind(provider='sqlite', filename='pony_test.db', create_db=True)
db.generate_mapping(create_tables=True)

