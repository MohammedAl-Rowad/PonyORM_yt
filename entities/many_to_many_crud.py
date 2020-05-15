from pony.orm import db_session
from datetime import datetime
import json
from faker import Faker
fake = Faker()

@db_session()
def fake_categories(Categories,amount = 10):
    categories = set()
    for i in range(amount):
        name = fake.first_name()
        if name not in categories: categories.add(name)
        else: amount += 1
    categories_list = list(categories)
    for category in categories_list: Categories(type=category)
    

@db_session()
def fake_categories_posts(Categories, Posts, PostsCategories, amount = 10):
    cat = Categories.select()
    for post in Posts.select(): 
        PostsCategories(post=post.id, category=fake.random_element(cat), custome_column=datetime.now())

@db_session()
def get_nested_data(Categories, Posts):
    print(
        json.dumps({'data': [p.to_dict() for p in Categories[1].posts_categories.post]}),
        json.dumps({'data2': [p.to_dict() for c in Categories.select() for p in c.posts_categories.post]}),
        # json.dumps({'data': p.to_dict() for p in Categories[1].posts_categories.post.user})
    )
    
    

