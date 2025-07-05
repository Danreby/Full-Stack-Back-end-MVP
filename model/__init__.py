
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.base import Base
from model.funcionario import Funcionario
from model.sectors import Sector

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "database")
os.makedirs(DB_DIR, exist_ok=True)

DATABASE_URL = f"sqlite:///{os.path.join(DB_DIR, 'db.sqlite3')}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}, 
    echo=True,                                 
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("✅ Banco de dados criado/atualizado em:", DATABASE_URL)
