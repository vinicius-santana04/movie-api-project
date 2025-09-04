from pymongo import MongoClient
import os

# Carrega as variáveis de ambiente
from dotenv import load_dotenv
load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")

# Cria o cliente do MongoDB
client = MongoClient(MONGODB_URL)

# Define o nome do banco de dados a ser usado
db = client["movie_db"]

# Função para obter o banco de dados
def get_nosql_db():
    return db