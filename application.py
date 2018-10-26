from flask import (Flask, render_template, request,
                   redirect, url_for, flash, jsonify)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from catalogDB_Model import Category, Item, User, Base
import datetime

from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response

# Appache 2
import requests

app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True
SEND_FILE_MAX_AGE_DEFAULT = 0

engine = create_engine('sqlite:///catalog.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

CLIENT_ID = json.loads(
    open('client_secrets.google.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog App"


# JSON Endpoints
@app.route('/catalog/JSON')
def catalonJSON():
    categories = session.query(Category).order_by(Category.name)
    return jsonify(Category=[i.serialize for i in categories])


@app.route('/catalog/<path:category_name>/items/JSON')
def itemsJSON(category_name):
    category = session.query(Category).filter_by(name=category_name)\
        .one_or_none()
    items = session.query(Item).filter_by(category_id=category.id)\
        .order_by(Item.name.desc())
    return jsonify(Item=[i.serialize for i in items])


@app.route('/catalog/<path:category_name>/<path:item_name>/JSON')
def itemsDetailsJSON(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name)\
        .one_or_none()
    item = session.query(Item).join(Category)\
        .filter(Category.id == category.id)\
        .filter(Item.name == item_name).one_or_none()
    return jsonify(Item=[item.serialize])


@app.route('/')
@app.route('/catalog/')
def showCatalog():
    categories = session.query(Category).order_by(Category.name)
    num_Categories = session.query(Category).count()
    # Sort by add date
    items = session.query(Item).order_by(Item.add_date.desc())\
        .limit(num_Categories)
    # Check login status for display the proper button
    loggedIn = logIn()
    return render_template('catalog.html', categories=categories,
                           items=items, loggedIn=loggedIn)


@app.route('/catalog/<path:category_name>/')
@app.route('/catalog/<path:category_name>/items/')
def showItems(category_name):
    """ List items in the specified category """
    categories = session.query(Category).order_by(Category.name)
    category = session.query(Category).filter_by(name=category_name)\
        .one_or_none()
    items = session.query(Item).filter_by(category_id=category.id)\
        .order_by(Item.name.desc())
    num_items = session.query(Item).filter_by(category_id=category.id).count()
    # Check login status for display the proper button
    loggedIn = logIn()
    return render_template('category.html', categories=categories,
                           category=category, count=num_items, items=items,
                           loggedIn=loggedIn)


@app.route('/catalog/<path:category_name>/<path:item_name>/')
def showItemsDetails(category_name, item_name):
    """ Display general item data """
    categories = session.query(Category).order_by(Category.name)
    category = session.query(Category).filter_by(name=category_name)\
        .one_or_none()
    item = session.query(Item).join(Category)\
        .filter(Category.id == category.id).filter(Item.name == item_name)\
        .one_or_none()
    # Check login status for display the proper button
    loggedIn = logIn()
    return render_template('item.html', categories=categories,
                           category=category, item=item, loggedIn=loggedIn)


@app.route('/catalog/newItem/', methods=['GET', 'POST'])
def newItem():
    """ Add an item to the database """
    loggedIn = logIn()
    # Redirect to login if not logged-in
    if not loggedIn:
        return redirect(url_for('showLogin'))
    categories = session.query(Category).order_by(Category.name)
    if request.method == 'POST':
        newItem = Item(name=request.form['name'],
                       description=request.form['description'],
                       price=request.form['price'],
                       category_id=request.form['itemCategory'],
                       add_date=datetime.datetime.now(),
                       user=getUserInfo(getUserID(login_session['email'])))
        session.add(newItem)
        session.commit()
        # Adding flash message
        flash("New Item Added")
        return redirect(url_for('showCatalog'))
    else:
        return render_template('newItem.html', categories=categories)


@app.route('/catalog/<path:item_name>/edit/', methods=['GET', 'POST'])
def editItem(item_name):
    """ Modify details of an existing item """
    loggedIn = logIn()
    # Redirect to login if not logged-in
    if not loggedIn:
        return redirect(url_for('showLogin'))
    categories = session.query(Category).order_by(Category.name)
    editIt = session.query(Item).filter(Item.name == item_name).one_or_none()
    # Confirm user owns/created the items
    if getUserID(login_session['email']) != editIt.user_id:
        return redirect(url_for('showCatalog'))
    if request.method == 'POST':
        if request.form['name']:
            if request.form['name'] != item_name:
                nameInUse = session.query(Item)\
                    .filter(Item.name == request.form['name']).count()
                # Check if new name already exists in the database
                if nameInUse != 0:
                    flash("Item not edited. An item by the desired new name"
                          " already exists.")
                    return redirect(url_for('showCatalog'))
            editIt.name = request.form['name']
        if request.form['description']:
            editIt.description = request.form['description']
        if request.form['price']:
            editIt.price = request.form['price']
        if request.form['itemCategory']:
            editIt.category_id = request.form['itemCategory']

        session.add(editIt)
        session.commit()
        # Adding flash message
        flash("Item Edited")
        return redirect(url_for('showCatalog'))
    else:
        return render_template('editItem.html', categories=categories,
                               item=editIt)


@app.route('/catalog/<path:item_name>/delete/', methods=['GET', 'POST'])
def deleteItem(item_name):
    """ Delete an item from the database """
    # Check login status for display the proper button
    loggedIn = logIn()
    if not loggedIn:
        return redirect(url_for('showLogin'))
    categories = session.query(Category).order_by(Category.name)
    deleteIt = session.query(Item).filter_by(name=item_name).one_or_none()
    # Check if user owns the item
    if getUserID(login_session['email']) != deleteIt.user_id:
        return redirect(url_for('showCatalog'))
    if request.method == 'POST':
        session.delete(deleteIt)
        session.commit()
        # Adding flash message
        flash("Item Successfully Deleted")
        return redirect(url_for('showCatalog'))
    return render_template('deleteItem.html', categories=categories,
                           item=deleteIt, loggedIn=loggedIn)


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    if 'username' in login_session:
        return redirect(url_for('showCatalog'))
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state, CLIENT_ID=CLIENT_ID)


# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    """ End Login for current authentication provider """
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['user_id']
        del login_session['email']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showCatalog'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showCatalog'))


@app.route('/gdisconnect')
def gdisconnect():
    """ End Login Via Google """
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given '
                                 'user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/fbdisconnect')
def fbdisconnect():
    """ End Login Via Facebook """
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % \
        (facebook_id, access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    return "you have been logged out"


@app.route('/gconnect', methods=['POST'])
def gconnect():
    """ Google Authentication """
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.google.json',
                                             scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already '
                                 'connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    # output = ''
    # output += '<h1>Welcome, '
    # output += login_session['username']
    # output += '!</h1>'
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    """ Facebook Authentication """
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print "access token received %s " % access_token

    app_id = json.loads(open('fb_client_secrets.json', 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_ty'\
        'pe=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token'\
        '=%s' % (app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.8/me"
    token = result.split(',')[0].split(':')[1].replace('"', '')

    url = 'https://graph.facebook.com/v2.8/me?access_token=%s&fields=name,id,'\
        'email' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    # print "url sent for API access:%s"% url
    # print "API JSON result: %s" % result
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token must be stored in the login_session in order to properly logout
    login_session['access_token'] = token

    # see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    # Add back after developing code to control display location
    # output = ''
    # output += '<h2>Welcome, '
    # output += login_session['username']
    # output += '!</h2>'

    flash("Now logged in as %s" % login_session['username'])
    return output


# User Helper Functions
# Add new user to database
def createUser(login_session):
    newUser = User(user_name=login_session['username'], email=login_session[
                   'email'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email'])\
        .one_or_none()
    return user.id


# Get Current user's data entry
def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one_or_none()
    return user


# Get Current users userID via email query
def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one_or_none()
        return user.id
    except Exception:
        return None


# Check if user logged In
def logIn():
    if 'username' in login_session:
        return True
    else:
        return False


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
