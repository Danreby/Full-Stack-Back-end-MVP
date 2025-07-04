# model/sector.py

from sqlalchemy import Column, Integer, String
from .base import Base

class Sector(Base):
    __tablename__ = 'sector'

    pk_sector = Column(Integer, primary_key=True)
    name      = Column(String(140), unique=True, nullable=False)

    def __init__(self, name: str):
        self.name = name
