import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable = False, unique = True)
    email = Column(String(50), nullable = False, unique = True)
    password = Column(String(10))
    planets = relationship("fav_Planets", backref="user" )
    characters = relationship("fav_Characters", backref="user" )

class Planets(Base):
    __tablename__ = 'planets'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))

class Fav_Characters(Base):
    __tablename__ = 'fav_characters'

    user_id = Column(Integer, ForeignKey("user.id"), nullable= False)
    characters_id = Column(Integer,ForeignKey("characters.id") , nullable= False)
    character = relationship("characters", backref="fav_characters" )

class Fav_Planets(Base):
    __tablename__ = 'fav_planets'
    
    user_id = Column(Integer, ForeignKey("user.id"), nullable= False)
    planets_id = Column(Integer,ForeignKey("planets.id"), nullable= False)
    planet = relationship("planets", backref="fav_planets" )





# class User(Base):
#     __tablename__ = 'User'

#     id = Column(Integer, primary_key=True)
#     name = String((50), nullable = False)
#     name = String((50), nullable = False)
#     email = Column(String(100), nullable = False, unique = True)
#     posts = relationship('Post', backref='users.id')