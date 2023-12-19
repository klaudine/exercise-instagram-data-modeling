import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(200), nullable=False)
    name = Column(String(200), nullable=False)
    email = Column(String(250), nullable=False, unique=True)

    posts = relationship('Post', back_populates='users')
    comments = relationship('Comment', back_populates='users')
    

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, nullable=False)
    person_id = Column(Integer, ForeignKey('user.id'))
    person = relationship(User)
    created = Column(DateTime)

    user = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='posts')

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, nullable=False)
    person_id = Column(Integer, ForeignKey('user.id'))
    person = relationship(User)
    created = Column(DateTime)

    user = relationship('User', back_populates='comments')
    posts = relationship('Post', back_populates='comments')

class Follower(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(200), nullable=False)
    name = Column(String(200), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    person = relationship(User)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
