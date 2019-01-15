from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('postgresql://catalog:catalog@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Dhafer ALamri", email="dhafer.a.alamri@gmail.com",
             picture='https://upload.wikimedia.org/wikipedia/commons/3/38/Wiki'
             'pedia_User-ICON_byNightsight.png')
session.add(User1)
session.commit()

# Menu for UrbanBurger
restaurant1 = Restaurant(user_id=1, name="Dhafer Burger")

session.add(restaurant1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Burger",
                     description="Juicy grilled veggie patty with tomato"
                     "mayo and lettuce",
                     price="$7.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="French Fries", description="with"
                     "garlic and parmesan",
                     price="$2.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

print "added menu items!"
