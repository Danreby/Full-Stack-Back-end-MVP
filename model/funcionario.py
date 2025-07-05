# model/funcionario.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from .base import Base
from .sectors import Sector

class Funcionario(Base):
    __tablename__ = 'funcionario'

    pk_funcionario = Column(Integer, primary_key=True)
    name           = Column(String(140), nullable=False)
    email          = Column(String(255), unique=True, nullable=False)
    sector_id      = Column(Integer, ForeignKey('sector.pk_sector'), nullable=False)
    sector         = relationship("Sector", backref="funcionarios")

    def __init__(
        self,
        name: str,
        email: str,
        sector: Union[Sector, int],
    ):
        self.name = name
        self.email = email
        if isinstance(sector, Sector):
            self.sector = sector
        else:
            self.sector_id = sector
