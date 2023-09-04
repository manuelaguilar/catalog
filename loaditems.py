from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, ProductCategory, CategoryItem, User

engine = create_engine('sqlite:///productcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Test user

testuser = User(name='TestUser', email='testuser@me.com', 
        picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(testuser)
session.commit()


# Test Category

user = session.query(User).filter_by(name='TestUser').one()
print("User id:", user.id)
testcategory = ProductCategory(name='Category1', user_id = user.id)
session.add(testcategory)
session.commit()

#testdupedcategory = ProductCategory(name='Category1', user_id = user.id)
#session.add(testdupedcategory)
#session.commit()

testcategory = session.query(ProductCategory).filter_by(name='Category1').one()
testitem = CategoryItem(name='Test Item', price='9.99', description='A test item', user_id=testuser.id, 
        product_category_id=testcategory.id)

session.add(testitem)
session.commit()

newcategory = ProductCategory(name='Category2', user_id = user.id)
session.add(newcategory)
session.commit()

testnewcategory = session.query(ProductCategory).filter_by(name='Category2').one()

testdupedname = CategoryItem(name='Test Item', price='1.11', description='Not the same', user_id=testuser.id,
        product_category_id=testnewcategory.id)

session.add(testdupedname)
session.commit()

# get items
items = session.query(CategoryItem).all()
for i in items:
    print(i.serialize)

