def def_users_entity(db, orm):
    class Users(db.Entity):
        _table_ = 'users'
        id = orm.PrimaryKey(int, auto=True)
        name = orm.Required(str, 40)
        age = orm.Required(int)
        about = orm.Optional(str, nullable=False)
        email = orm.Required(str, unique=True)
