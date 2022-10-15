# models.py

# from hello import db
from sqlalchemy.sql import func

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

from database import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    url_profile = Column(String(250), nullable=True)
    created_at = Column(DateTime(timezone=True),
                           server_default=func.now())
    bio = Column(Text)

    def __repr__(self):
        return f'<User {self.email}>'



# class Project(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text)
#     created_at = db.Column(db.DateTime(timezone=True),
#                            server_default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # get user_id => project.user.id

#     def __repr__(self):
#         return f'<Project "{self.content[:20]}...">' 



Base.metadata.create_all(engine)
