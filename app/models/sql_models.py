from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database.sql import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    imdb_rating = Column(Float)
    imdb_votes = Column(Integer)
    release_date = Column(Date)
    runtime = Column(Integer)
    original_language = Column(String)
    overview = Column(String)
    popularity = Column(Float)
    genres = Column(String)
    director = Column(String)
    cast = Column(String)

    # Relacionamento com a tabela de avaliações
    ratings = relationship("Rating", back_populates="movie")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # Relacionamento com a tabela de avaliações
    ratings = relationship("Rating", back_populates="user")

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    movie_id = Column(Integer, ForeignKey("movies.id"))
    rating = Column(Float)

    # Definição dos relacionamentos
    user = relationship("User", back_populates="ratings")
    movie = relationship("Movie", back_populates="ratings")

