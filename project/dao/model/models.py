# from sqlalchemy import Column, String, Float, Integer, ForeignKey
# from sqlalchemy.orm import relationship
#
# from project.setup.db import models
#
#
# class Genre(models.Base):
#     __tablename__ = 'genre'
#
#     name = Column(String(100), unique=True, nullable=False)
#
#
# class Director(models.Base):
#     __tablename__ = 'director'
#
#     name = Column(String(100), unique=True, nullable=False)
#
#
# class Movie(models.Base):
#     __tablename__ = 'movie'
#
#     title = Column(String(100))
#     description = Column(String(250))
#     trailer = Column(String(200))
#     year = Column(Integer)
#     rating = Column(Float(100))
#     genre_id = Column(Integer, ForeignKey("genre.id"))
#     genre = relationship("Genre")
#     director_id = Column(Integer, ForeignKey("director.id"))
#     director = relationship("Director")
#
#
# class User(models.Base):
#     __tablename__ = 'user'
#
#     email = Column(String(100), unique=True, nullable=False)
#     password = Column(String(100), nullable=False)
#     name = Column(String(100), nullable=False)
#     surname = Column(String(100))
#     favorite_genre = Column(String(100))
