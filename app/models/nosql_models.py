from pydantic import BaseModel
from typing import Optional, List
from datetime import date


# Base para todos os modelos da API
class MovieBase(BaseModel):
    title: str
    imdb_rating: Optional[float] = None
    imdb_votes: Optional[int] = None
    release_date: Optional[date] = None
    runtime: Optional[int] = None
    original_language: Optional[str] = None
    overview: Optional[str] = None
    popularity: Optional[float] = None
    genres: Optional[str] = None
    director: Optional[str] = None
    cast: Optional[str] = None


# Modelo de resposta para um filme
class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


# Modelo para um usuário
class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


# Modelo para uma avaliação
class RatingBase(BaseModel):
    user_id: int
    movie_id: int
    rating: float


class RatingCreate(BaseModel):
    rating: float


class Rating(RatingBase):
    id: int

    class Config:
        orm_mode = True