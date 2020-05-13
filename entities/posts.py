def def_posts_entity(db, orm, Users):
    class Posts(db.Entity):
        _table_ = 'posts'
        id = orm.PrimaryKey(int, auto=True)
        title = orm.Required(str, 40)
        body = orm.Required(str)
        user = orm.Required(Users, column='user_id') # will create a column named user(int) by default
