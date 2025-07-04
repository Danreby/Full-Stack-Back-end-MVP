# generate_db.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# importa seu Base e modelos pra serem registrados no metadata
from model.base import Base
from model.funcionario import Funcionario
from model.sectors import Sector

# 1) garante que a pasta “database/” existe
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "database")
os.makedirs(DB_DIR, exist_ok=True)

# 2) define a URL do SQLite (arquivo em database/db.sqlite3)
DATABASE_URL = f"sqlite:///{os.path.join(DB_DIR, 'db.sqlite3')}"

# 3) cria engine e session factory
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # necessário pro SQLite
    echo=True,                                 # mostra SQL no console (opcional)
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# 4) cria as tabelas no banco, se ainda não existirem
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("✅ Banco de dados criado/atualizado em:", DATABASE_URL)
