# Catalog App

Catalog App is a web application for catagloing jewerly craftig items.

  - Items grouped into catagories
  - Item modification authentication protected
  - Third party login authentication

### How to Execute the App

Catalog App uses a number of open source projects to work properly:

1.	Install Vagrant and VirtualBox
2.	Clone the fullstack-nanodegree-vm
3.	Launch the Vagrant VM (vagrant up)
4.	Write your Flask application locally in the vagrant/catalog directory (which will automatically be synced to /vagrant/catalog within the VM).
5.  Run your application within the VM. Execute command 6 - 9
6.  python /vagrant/catalog/catalogDB_Model.py
7.  python /vagrant/catalog/lotofitems.py
8.  python /vagrant/catalog/application.py)
9.	Access and test your application by visiting http://localhost:8000 locally

### JSON Endpoints

1.  List of categores
   - http://localhost:8000/catalog/JSON

2.  Replace category_name with the name of the desired category
   - [http://localhost:8000/catalog/category_name/items/JSON]

3.  Replace category_name with the name of the desired category and item_name with the name of the desired item
   - [http://localhost:8000/catalog/category_name/item_name/JSON]

### Installation
1. Clone or download https://github.com/ladytrell/catalog_project to to /vagrant/catalog
2. Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

### Todos

 - Control display location of login welcome
 - Responsive flow

License
----

MIT


**Free Software**
