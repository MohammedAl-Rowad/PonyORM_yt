def def_categories_entity(db, orm):
    class Categories(db.Entity):
        _table_ = 'categories'
        id = orm.PrimaryKey(int, auto=True)
        type = orm.Required(str, 40, unique=True, nullable=False)
        posts_categories = orm.Set('PostsCategories') # refrence the class name not __table__
    return Categories
