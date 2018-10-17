from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from catalogDB_Model import Category, Item, Base

app = Flask(__name__)


engine = create_engine('sqlite:///catalog.db', connect_args={'check_same_thread':False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/catalog/')
def showCatalog():
    categories = session.query(Category).order_by(Category.name)
    num_Categories = session.query(Category).count()
    #Sort by add date
    items = session.query(Item).order_by(Item.add_date.desc()).limit(num_Categories)
    return render_template('catalog.html', categories = categories, items = items)

@app.route('/catalog/<int:category_id>/')
@app.route('/catalog/<int:category_id>/items/')
def showItems(category_id):    
    categories = session.query(Category).order_by(Category.name)
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id).order_by(Item.name.desc())
    num_items = session.query(Item).filter_by(category_id=category_id).count()
    #return("This page will show all my catalog")
    return render_template('category.html', categories = categories, category = category, count = num_items, items = items)

@app.route('/catalog/<int:category_id>/items/')
def showItems(category_id):    
    categories = session.query(Category).order_by(Category.name)
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id).order_by(Item.name.desc())
    num_items = session.query(Item).filter_by(category_id=category_id).count()
    #return("This page will show all my catalog")
    return render_template('category.html', categories = categories, category = category, count = num_items, items = items)
    
if __name__ == '__main__':
    #
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)