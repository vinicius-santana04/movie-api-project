from app.database.sql import engine, Base
from app.models.sql_models import Movie, User, Rating

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)
