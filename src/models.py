import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    diameter = Column(String(250), nullable=True)
    population = Column(Integer)
    gravity = Column(String(250))
    climate = Column(String(250))
   

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
    last_name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    planet_id = Column(Integer,ForeignKey('planet.id'))
    

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_favorito = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_planet = Column(Integer, ForeignKey('planet.id'))
    id_character = Column(Integer, ForeignKey('personaje.id'))
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
