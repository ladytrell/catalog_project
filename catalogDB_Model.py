import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context


Base = declarative_base()


# User table
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    email = Column(String)


# Category table
class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'category': self.category,
            }


# Item table
class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(String(8))
    add_date = Column(Date)
    category = relationship(Category)
    category_id = Column(Integer, ForeignKey('category.id'))
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'price': self.price
            }


engine = create_engine('sqlite:///catalog.db',
                       connect_args={'check_same_thread': False})


Base.metadata.create_all(engine)
