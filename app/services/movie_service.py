from sqlalchemy.orm import Session
from typing import List
from app.models.sql_models import Movie as SQLMovie

# Função para obter um filme por ID
def get_movie(db: Session, movie_id: int):
    return db.query(SQLMovie).filter(SQLMovie.id == movie_id).first()

# Função para obter uma lista de filmes
def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SQLMovie).offset(skip).limit(limit).all()