
from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship



class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index= True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('newusers.id'))

    creator = relationship("NewUser", back_populates="blogs")


# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String)
#     password = Column(String)  


class NewUser(Base):
    __tablename__ = 'newusers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('Blog', back_populates="creator")

