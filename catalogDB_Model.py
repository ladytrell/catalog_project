import os
import sys
from sqlalchemy import (Column, ForeignKey, Integer, String, Date,
                        PrimaryKeyConstraint, UniqueConstraint,
                        ForeignKeyConstraint)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context


Base = declarative_base()


# User table
class User(Base):
    """
    Registered user data for database
    """
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False,)
    email = Column(String)
    items = relationship("Item", cascade="all, delete-orphan")


# Category table
class Category(Base):
    """
    Categories for the catalog database
    """
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    items = relationship("Item", cascade="all, delete-orphan")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'category': self.category,
            }


# Item table
class Item(Base):
    """
    Item data for database
    """
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String)
    price = Column(String(8))
    add_date = Column(Date)
    category = relationship(Category)
    category_id = Column(Integer, ForeignKey('category.id'))
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'price': self.price,
            'category_id': self.category_id,
            'user_id': self.user_id
            }


engine = create_engine('sqlite:///catalog.db',
                       connect_args={'check_same_thread': False})


Base.metadata.create_all(engine)
