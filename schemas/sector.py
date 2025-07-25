from pydantic import BaseModel, Field
from typing import List, Optional
from model.sectors import Sector
from schemas.funcionario import FuncionarioViewSchema

class SectorSchema(BaseModel):
    """Define como um novo setor a ser inserido deve ser representado"""
    name: str = Field(..., example="TI")

class SectorBuscaSchema(BaseModel):
    """Define como a busca de setor deve ser representada (por ID)."""
    id: int = 1

class SectorViewSchema(BaseModel):
    id: int
    name: str
    funcionarios: Optional[List[FuncionarioViewSchema]] = None

class ListagemSectorsSchema(BaseModel):
    """Define como a listagem de setores será retornada"""
    sectors: List[SectorViewSchema]

class SectorDelSchema(BaseModel):
    """Define como é a resposta de uma remoção de setor."""
    message: str
    id: int

def apresenta_sectors(sectors: List[Sector]):
    """Retorna uma representação de vários setores seguindo ListagemSectorsSchema."""
    result = []
    for s in sectors:
        result.append({
            "id": s.pk_sector if hasattr(s, 'pk_sector') else s.id,
            "name": s.name,
            "funcionarios": [
                {
                    "id": f.pk_funcionario if hasattr(f, 'pk_funcionario') else f.id,
                    "name": f.name,
                    "email": f.email,
                }
                for f in getattr(s, 'funcionarios', [])
            ]
        })
    return {"sectors": result}


def apresenta_sector(sector: Sector):
    """Retorna uma representação de um setor seguindo SectorViewSchema."""
    return {
        "id": sector.pk_sector if hasattr(sector, 'pk_sector') else sector.id,
        "name": sector.name,
        "funcionarios": [
            {
                "id": f.pk_funcionario if hasattr(f, 'pk_funcionario') else f.id,
                "name": f.name,
                "email": f.email,
            }
            for f in getattr(sector, 'funcionarios', [])
        ]
    }

def apresenta_setor_deletado(id: int):
    """Retorna mensagem de confirmação de remoção de setor seguindo SectorDelSchema."""
    return {"message": "Setor removido com sucesso.", "id": id}

def apresenta_setor_atualizado(sector: Sector):
    """Retorna representação de setor atualizado seguindo SectorViewSchema."""
    return apresenta_sector(sector)
