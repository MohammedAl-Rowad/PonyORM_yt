
def def_users_entity(db, orm):
    class Users(db.Entity):
        _table_ = 'users'
        id = orm.PrimaryKey(int, auto=True)
        first_name = orm.Required(str, 40)
        second_name = orm.Required(str, 40)
        # name = Required(str, column="person_name")
        age = orm.Required(int)
        about = orm.Optional(str, nullable=False)
        email = orm.Required(str, unique=True)
        posts = orm.Set('Posts') # refrence the class name not __table__
    return Users
