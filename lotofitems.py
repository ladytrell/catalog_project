from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
 
from catalogDB_model import Category, Base, Item, User
 
engine = create_engine('sqlite:///catalog.db', connect_args={'check_same_thread':False})
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



user1 = User(user_name = "Antrell Kent", id = 1, email = "antrell.d.e@gmail.com")
session.add(user1)
session.commit()

#Menu for UrbanBurger
category1 = Category(name = "Findings")

session.add(category1)
session.commit()

item2 = Item(name = "Veggie Burger", description = "Juicy grilled veggie patty with tomato mayo and lettuce", price = "$7.50", add_date = datetime(2016, 9, 27), category = category1)

session.add(item2)
session.commit()


item1 = Item(name = "French Fries", description = "with garlic and parmesan", price = "$2.99", add_date = datetime(2017, 4, 11), category = category1)

session.add(item1)
session.commit()

item2 = Item(name = "Chicken Burger", description = "Juicy grilled chicken patty with tomato mayo and lettuce", price = "$5.50", add_date = datetime(2016, 9, 27), category = category1)

session.add(item2)
session.commit()

item3 = Item(name = "Chocolate Cake", description = "fresh baked and served with ice cream", price = "$3.99", add_date = datetime(2000, 2, 14), category = category1)

session.add(item3)
session.commit()

item4 = Item(name = "Sirloin Burger", description = "Made with grade A beef", price = "$7.99", add_date = datetime(2016, 9, 27), category = category1)

session.add(item4)
session.commit()

item5 = Item(name = "Root Beer", description = "16oz of refreshing goodness", price = "$1.99", add_date = datetime(1999, 5, 24), category = category1)

session.add(item5)
session.commit()

item6 = Item(name = "Iced Tea", description = "with Lemon", price = "$.99", add_date = datetime(1999, 5, 24), category = category1)

session.add(item6)
session.commit()

item7 = Item(name = "Grilled Cheese Sandwich", description = "On texas toast with American Cheese", price = "$3.49", add_date = datetime(2016, 9, 27), category = category1)

session.add(item7)
session.commit()



#Menu for Super Stir Fry
category2 = Category(name = "Beads & Pearls")

session.add(category2)
session.commit()


item1 = Item(name = "Chicken Stir Fry", description = "With your choice of noodles vegetables and sauces", price = "$7.99", add_date = datetime(2016, 9, 27), category = category2)

session.add(item1)
session.commit()

item2 = Item(name = "Peking Duck", description = " A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price = "$25", add_date = datetime(2016, 9, 27), category = category2)

session.add(item2)
session.commit()

item3 = Item(name = "Spicy Tuna Roll", description = "Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ", price = "15", add_date = datetime(2016, 9, 27), category = category2)

session.add(item3)
session.commit()

item4 = Item(name = "Nepali Momo ", description = "Steamed dumplings made with vegetables, spices and meat. ", price = "12", add_date = datetime(2016, 9, 27), category = category2)

session.add(item4)
session.commit()

item5 = Item(name = "Beef Noodle Soup", description = "A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.", price = "14", add_date = datetime(2016, 9, 27), category = category2)

session.add(item5)
session.commit()

item6 = Item(name = "Ramen", description = "a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.", price = "12", add_date = datetime(2016, 9, 27), category = category2)

session.add(item6)
session.commit()



#Beading Supplies
category1 = Category(name = "Beading Supplies")

session.add(category1)
session.commit()


item1 = Item(name = "Bolo Tie Kit", description = "Each kit includes a black leather bolo cord, with silver color bolo tips, a silver bolo clasp and E6000 glue to attach your favorite decorative accent to the front of the clasps.", price = "$6.95", add_date = datetime(2016, 9, 27), category = category1, user = user1)

session.add(item1)
session.commit()

item2 = Item(name = "Silver Beading Wire", description = "beading wire is composed of stainless steel wire that is coated with clear, soft nylon. 7 strand is used for most general beading and craft designs.", price = "$3.99", add_date = datetime(2017, 4, 11), category = category1, user = user1)

session.add(item2)
session.commit()

item3 = Item(name = "Tiger Tail Flexible Wire", description = "Ta Nylon coated wire, which will not stretch, yet is flexible enough to be knotted and tied. The Nylon coating on Tiger Tail Wire prevents ""sawing"" or ""cutting"" into Beads, Clasps, and Connectors.", price = "$2.95", add_date = datetime(2016, 9, 27), category = category1, user = user1)

session.add(item3)
session.commit()

item4 = Item(name = "Suede Cord", description = "Black real suede, 3 x 3mm, 1 yard", price = "$1.99", add_date = datetime(2016, 9, 27), category = category1, user = user1)

session.add(item4)
session.commit()


#Menu for Thyme for that
category1 = Category(name = "Wire, Chain, & Metal")

session.add(category1)
session.commit()


item1 = Item(name = "Tres Leches Cake", description = "Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.", price = "$2.99", add_date = datetime(2000, 2, 14), category = category1)

session.add(item1)
session.commit()

item2 = Item(name = "Mushroom risotto", description = "Portabello mushrooms in a creamy risotto", price = "$5.99", add_date = datetime(2016, 9, 27), category = category1)

session.add(item2)
session.commit()

item3 = Item(name = "Honey Boba Shaved Snow", description = "Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi", price = "$4.50", add_date = datetime(2000, 2, 14), category = category1)

session.add(item3)
session.commit()

item4 = Item(name = "Cauliflower Manchurian", description = "Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions", price = "$6.95", add_date = datetime(2017, 4, 11), category = category1)

session.add(item4)
session.commit()

item5 = Item(name = "Aloo Gobi Burrito", description = "Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom", price = "$7.95", add_date = datetime(2016, 9, 27), category = category1)

session.add(item5)
session.commit()


#Menu for Tony's Bistro
category1 = Category(name = "Tools")

session.add(category1)
session.commit()


item1 = Item(name = "Shellfish Tower", description = "Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower", price = "$13.95", add_date = datetime(2016, 9, 27), category = category1)

session.add(item1)
session.commit()

item2 = Item(name = "Chicken and Rice", description = "Chicken... and rice", price = "$4.95", add_date = datetime(2016, 9, 27), category = category1)

session.add(item2)
session.commit()

item3 = Item(name = "Mom's Spaghetti", description = "Spaghetti with some incredible tomato sauce made by mom", price = "$6.95", add_date = datetime(2016, 9, 27), category = category1)

session.add(item3)
session.commit()

item4 = Item(name = "Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)", description = "Milk, cream, salt, ..., Liquid nitrogen magic", price = "$3.95", add_date = datetime(2000, 2, 14), category = category1)

session.add(item4)
session.commit()

item5 = Item(name = "Tonkatsu Ramen", description = "Noodles in a delicious pork-based broth with a soft-boiled egg", price = "$7.95", add_date = datetime(2016, 9, 27), category = category1)

session.add(item5)
session.commit()



#Menu for Andala's 
category1 = Category(name = "Displays & Packaging")

session.add(category1)
session.commit()


item1 = Item(name = "Lamb Curry", description = "Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.", price = "$9.95", add_date = datetime(2016, 9, 27), category = category1)

session.add(item1)
session.commit()

item2 = Item(name = "Chicken Marsala", description = "Chicken cooked in Marsala wine sauce with mushrooms", price = "$7.95", add_date = datetime(2016, 9, 27), category = category1)

session.add(item2)
session.commit()

item3 = Item(name = "Potstickers", description = "Delicious chicken and veggies encapsulated in fried dough.", price = "$6.50", add_date = datetime(2017, 4, 11), category = category1)

session.add(item3)
session.commit()

item4 = Item(name = "Nigiri Sampler", description = "Maguro, Sake, Hamachi, Unagi, Uni, TORO!", price = "$6.75", add_date = datetime(2017, 4, 11), category = category1)

session.add(item4)
session.commit()

item2 = Item(name = "Shrimp N' Grits", description = "Low country jumbo shrimp, seasoned garlic, onion, chicken sausage served over smooth grits", price = "$13.50", add_date = datetime(2018, 10, 2), category = category1)

session.add(item2)
session.commit()


#Menu for Auntie Ann's
category1 = Category(name = "Crystals")

session.add(category1)
session.commit()

item9 = Item(name = "Chicken Fried Steak", description = "Fresh battered sirloin steak fried and smothered with cream gravy", price = "$8.99", add_date = datetime(2016, 9, 27), category = category1)

session.add(item9)
session.commit()



item1 = Item(name = "Boysenberry Sorbet", description = "An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness", price = "$2.99", add_date = datetime(2000, 2, 14), category = category1)

session.add(item1)
session.commit()

item2 = Item(name = "Broiled salmon", description = "Salmon fillet marinated with fresh herbs and broiled hot & fast", price = "$10.95", add_date = datetime(2016, 9, 27), category = category1)

session.add(item2)
session.commit()

item3 = Item(name = "Morels on toast (seasonal)", description = "Wild morel mushrooms fried in butter, served on herbed toast slices", price = "$7.50", add_date = datetime(2017, 4, 11), category = category1)

session.add(item3)
session.commit()

item4 = Item(name = "Tandoori Chicken", description = "Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.", price = "$8.95", add_date = datetime(2016, 9, 27), category = category1)

session.add(item4)
session.commit()

item10 = Item(name = "Spinach Ice Cream", description = "vanilla ice cream made with organic spinach leaves", price = "$1.99", add_date = datetime(2000, 2, 14), category = category1)

session.add(item10)
session.commit()


print "added items!"