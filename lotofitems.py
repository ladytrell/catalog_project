from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from catalogDB_model import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db',
                       connect_args={'check_same_thread': False})
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


user1 = User(user_name="Antrell Kent", email="antrell.d.e@gmail.com")
session.add(user1)
session.commit()

user2 = User(user_name="Antrell Kent", email="ladytrell@hotmail.com")
session.add(user2)
session.commit()

# Item descriptions and prices from https://www.jewelrysupply.com and
# https://www.firemountaingems.com

# Findings
category1 = Category(name="Findings")

session.add(category1)
session.commit()

item2 = Item(name="Round Jump Rings",
             description="3mm 10k Gold open connection ring (10-Pc)",
             price="$27.50", add_date=datetime(2016, 9, 27),
             category=category1, user=user2)

session.add(item2)
session.commit()


item1 = Item(name="Triange Jump Rings",
             description="4mm 10k Gold open connection ring (10-Pc)",
             price="$35.50", add_date=datetime(2017, 4, 11),
             category=category1, user=user2)

session.add(item1)
session.commit()

item2 = Item(name="Lobster Clasps",
             description="(1 Pc)Sterling Silver Clasp with spring loaded "
             "trigger mechanism is always in the locked position, unless "
             "manually opened, so it is almost impossible for the Clasp to "
             "come open on items own.",
             price="$1.50", add_date=datetime(2016, 9, 27),
             category=category1, user=user2)

session.add(item2)
session.commit()

item3 = Item(name="S Clasp",
             description="S shaped closure with closed jump rings (5 Pc) "
             "Stainless Steel", price="$3.99",
             add_date=datetime(2000, 2, 14), category=category1, user=user2)

session.add(item3)
session.commit()

item4 = Item(name="Cord end", description="Fold over stain less closure "
             "for ends of string material (10 Pc)", price="$5.99",
             add_date=datetime(2016, 9, 27), category=category1,
             user=user2)

session.add(item4)
session.commit()


# Menu for Beads & Pearls
category2 = Category(name="Beads & Pearls")

session.add(category2)
session.commit()


item1 = Item(name="Button Pearl", description="Freshwater Button Pearl "
             "White 2.5-3mm (16"" Strand)", price="$16.99",
             add_date=datetime(2016, 9, 27), category=category2)

session.add(item1)
session.commit()

item2 = Item(name="Corrugated Metal Bead", description="Corrugated Bead "
             "3mm Round Silver Plated (10-Pcs)", price="$0.35",
             add_date=datetime(2016, 9, 27), category=category2)

session.add(item2)
session.commit()

item3 = Item(name="Amethyst Bead", description="Amethyst Faceted Beads "
             "2mm (13 Inch Strand)", price="$10.99",
             add_date=datetime(2016, 9, 27), category=category2)

session.add(item3)
session.commit()

item4 = Item(name="Stopper Bead", description="Smart Bead Round 7mm "
             "Sterling Silver (1-Pc)", price="$1.00",
             add_date=datetime(2016, 9, 27), category=category2)

session.add(item4)
session.commit()

item5 = Item(name="Wooden Bead", description="Bleached Wood Grooved Oval "
             "Bead 25x20mm (10-Pc)", price="$6.00",
             add_date=datetime(2016, 9, 27), category=category2)

session.add(item5)
session.commit()


# Beading Supplies
category1 = Category(name="Beading Supplies")

session.add(category1)
session.commit()


item1 = Item(name="Bolo Tie Kit", description="Each kit includes a black "
             "leather bolo cord, with silver color bolo tips, a silver bolo "
             "clasp and E6000 glue to attach your favorite decorative accent "
             "to the front of the clasps.", price="$6.95",
             add_date=datetime(2016, 9, 27), category=category1, user=user1)

session.add(item1)
session.commit()

item2 = Item(name="Silver Beading Wire", description="beading wire is "
             "composed of stainless steel wire that is coated with clear, "
             "soft nylon. 7 strand is used for most general beading and "
             "craft designs.", price="$3.99", add_date=datetime(2017, 4, 11),
             category=category1, user=user1)

session.add(item2)
session.commit()

item3 = Item(name="Tiger Tail Flexible Wire", description="Ta Nylon coated "
             "wire, which will not stretch, yet is flexible enough to be "
             "knotted and tied. The Nylon coating on Tiger Tail Wire "
             "prevents ""sawing"" or ""cutting"" into Beads, Clasps, and "
             "Connectors.", price="$2.95", add_date=datetime(2016, 9, 27),
             category=category1, user=user1)

session.add(item3)
session.commit()

item4 = Item(name="Suede Cord", description="Black real suede, 3 x 3mm, 1 "
             "yard", price="$1.99", add_date=datetime(2016, 9, 27),
             category=category1, user=user1)

session.add(item4)
session.commit()

item2 = Item(name="Jump Rings", description="3mm 10k Gold Round Open (10-Pc)",
             price="$27.50", add_date=datetime(2016, 9, 27),
             category=category1, user=user1)

session.add(item2)
session.commit()


# Wire, Chain, & Metal
category1 = Category(name="Wire, Chain, & Metal")

session.add(category1)
session.commit()


item1 = Item(name="Yellow Gold Wire", description="14k Yellow Gold Wire Round"
             " 20ga (1-Inch)", price="$10.99", add_date=datetime(2000, 2, 14),
             category=category1, user=user1)

session.add(item1)
session.commit()

item2 = Item(name="Stainless Steel Wire", description="Stainless Steel Wire "
             "Round 22ga (33 Feet)", price="$7.50",
             add_date=datetime(2016, 9, 27), category=category1, user=user1)

session.add(item2)
session.commit()

item3 = Item(name="Bulk Chain Antique Copper Plated", description="Flat Long "
             "and Short Chain 6mm Antique Copper Plated (1-Ft)",
             price="$1.50", add_date=datetime(2000, 2, 14),
             category=category1, user=user1)

session.add(item3)
session.commit()

item4 = Item(name="Bulk Sterling Silver Wire", description="Sterling Silver "
             "Wire Round Dead Soft 24ga (1-Ft)", price="$2.25",
             add_date=datetime(2017, 4, 11), category=category1, user=user1)

session.add(item4)
session.commit()

item5 = Item(name="Bulk Copper Wire", description="VBare Copper Wire Dead "
             "Soft Round 22ga (20-Ft)", price="$4.95",
             add_date=datetime(2016, 9, 27), category=category1, user=user1)

session.add(item5)
session.commit()


# Menu for Tools
category1 = Category(name="Tools")

session.add(category1)
session.commit()


item1 = Item(name="Bead Reamer Set", description="This Bead Reamer Set "
             "includes four Diamond tipped Reamers, which are perfect for "
             "smoothing rough edges or enlarging holes on Pearls and Beads. "
             "Each Reamer is set into a hard Plastic Handle, allowing for "
             "better control of the Reamer.", price="$4.95",
             add_date=datetime(2016, 9, 27), category=category1, user=user1)

session.add(item1)
session.commit()

item2 = Item(name="Gold Tester", description="Kent Inc PLUS Electronic Gold "
             "Tester & Platinum Tester", price="$500.00",
             add_date=datetime(2016, 9, 27), category=category1, user=user1)

session.add(item2)
session.commit()

item3 = Item(name="Chain Nose Pliers", description="Made of stainless steel, "
             "2K Ecco Chain Nose Pliers (Needle Nose Pliers) feature a "
             "brushed metal finish, and non-slip PVC grips.", price="$9.95",
             add_date=datetime(2016, 9, 27), category=category1, user=user1)

session.add(item3)
session.commit()

item4 = Item(name="Wire Wrapping Mandrels (Pack of 2)", description="This two"
             " piece 6 mandrel set made of stainless steel with a non-slip "
             "PVC handle will give the user consistent size loops time after "
             "time.", price="$19.95", add_date=datetime(2000, 2, 14),
             category=category1, user=user1)

session.add(item4)
session.commit()

item5 = Item(name="Jewelry Soldering Kit", description="Ten piece Soldering "
             "Kit includes all the essential tools for basic soldering, but "
             "unlike other Soldering Kits which may look the same, our kit "
             "features a specially designed, taller tripod and mesh screen.",
             price="$135.95", add_date=datetime(2016, 9, 27),
             category=category1, user=user1)

session.add(item5)
session.commit()


# Displays & Packaging
category1 = Category(name="Displays & Packaging")

session.add(category1)
session.commit()


item1 = Item(name="Jewelry Display Hump for Bracelets", description="Steel "
             "Gray Half Moon Bracelet Jewelry Display is great for displaying"
             " jewelry in showcases, on countertops or at tradeshows. Size "
             "(W x D x H): 8-1/4"" x 5"" x 2-1/2"" Gray Leatherette",
             price="$5.95", add_date=datetime(2016, 9, 27),
             category=category1, user=user1)

session.add(item1)
session.commit()

item2 = Item(name="Jewelry Display Bracelet Ramp", description="Black Velvet "
             "Jewelry Display Ramp with 9 ribs is great for displaying up to "
             "nine bracelets or small watches.", price="$5.95",
             add_date=datetime(2016, 9, 27), category=category1, user=user1)

session.add(item2)
session.commit()

item3 = Item(name="Hanging Earring Card", description="Hanging card with "
             "pre-punched holes for Stud Earrings, Hoop Earrings, and Dangle "
             "Earrings (100 count)", price="$10.50",
             add_date=datetime(2017, 4, 11), category=category1, user=user1)

session.add(item3)
session.commit()

item4 = Item(name="Polka Dot Jewelry Box #21 (100-Pcs)",
             description="Assorted colored polka dot pattern boxes with "
             "cotton Size: 2-5/8"" x 1-1/2"" x 1""H", price="$28.75",
             add_date=datetime(2017, 4, 11), category=category1, user=user1)

session.add(item4)
session.commit()

item2 = Item(name="Black Necklace Busts Jewelry Display Kit (5-Piece)",
             description="Kit includes: (1) 10"" Bust, (1) 7"" Bust, (1) 6"" "
             "Bust and (2) Lay Down Busts", price="$13.50",
             add_date=datetime(2018, 10, 2), category=category1, user=user1)

session.add(item2)
session.commit()


# Crystals
category1 = Category(name="Crystals")

session.add(category1)
session.commit()

item1 = Item(name="Ocean Crystal Bead mix", description="7.5-8mm faceted "
             "round beads in an aquatic palette. Sold per pkg of 40.",
             price="$2.60", add_date=datetime(2000, 2, 14),
             category=category1, user=user1)

session.add(item1)
session.commit()

item2 = Item(name="Crystal Bead with gold-finished brass",
             description="32-facet, black, 13x9mm-14x10mm faceted rondelle "
             "with 4.5mm hole. Sold per pkg of 10.", price="$10.95",
             add_date=datetime(2016, 9, 27), category=category1, user=user1)

session.add(item2)
session.commit()

item3 = Item(name="Fall Crystal Drop mix", description="11.5x5.5mm-12.5x6mm "
             "faceted briolette drops in a warm autumnal palette. Sold per "
             "pkg of 40.", price="$7.50", add_date=datetime(2017, 4, 11),
             category=category1, user=user1)

session.add(item3)
session.commit()

item4 = Item(name="Swarovski 6533 Raindrop Pendant", description="17mm "
             "Crystal Bermuda Blue Rhodium Plated (1-Pc)", price="$5.95",
             add_date=datetime(2016, 9, 27), category=category1, user=user1)

session.add(item4)
session.commit()

item10 = Item(name="Swarovski 5328 2.5mm Crystal Bicone Bead Factory Pack",
              description=" 1440 precision faceted crystal beads sealed in a "
              "master factory pack.", price="$168.99",
              add_date=datetime(2000, 2, 14), category=category1, user=user1)

session.add(item10)
session.commit()


print "added items!"
