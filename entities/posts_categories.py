from datetime import datetime
def def_posts_categories_entity(db, orm, Posts, Categories):
    class PostsCategories(db.Entity):
        _table_ = 'posts_categories'
        id = orm.PrimaryKey(int, auto=True)
        post = orm.Required(Posts, column='post_id')
        category = orm.Required(Categories, column='category_id')
        custome_column = orm.Required(datetime)
    return PostsCategories