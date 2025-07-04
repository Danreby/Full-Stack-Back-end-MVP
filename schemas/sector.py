from pydantic import BaseModel, Field
from typing import List, Optional
from model.sectors import Sector
from schemas.funcionario import FuncionarioViewSchema

# ─── CREATE ─────────────────────────────────────────────────────────
class SectorSchema(BaseModel):
    """Define como um novo setor a ser inserido deve ser representado"""
    name: str = Field(..., example="TI")

# ─── READ (single) ───────────────────────────────────────────────────
class SectorBuscaSchema(BaseModel):
    """Define como a busca de setor deve ser representada (por ID)."""
    id: int = 1

# sector.py
class SectorViewSchema(BaseModel):
    id: int
    name: str
    funcionarios: Optional[List[FuncionarioViewSchema]] = None

# ─── READ (list) ─────────────────────────────────────────────────────
class ListagemSectorsSchema(BaseModel):
    """Define como a listagem de setores será retornada"""
    sectors: List[SectorViewSchema]

# ─── DELETE ──────────────────────────────────────────────────────────
class SectorDelSchema(BaseModel):
    """Define como é a resposta de uma remoção de setor."""
    message: str
    id: int

# ─── FUNÇÕES DE APRESENTAÇÃO ─────────────────────────────────────────
def apresenta_sectors(sectors: List[Sector]):
    """Retorna uma representação de vários setores seguindo ListagemSectorsSchema."""
    result = []
    for s in sectors:
        result.append({
            "id": s.pk_sector if hasattr(s, 'pk_sector') else s.id,
            "name": s.name,
            # se o setor tiver relação de funcionários
            "funcionarios": [
                {
                    "id": f.pk_funcionario if hasattr(f, 'pk_funcionario') else f.id,
                    "name": f.name,
                    "email": f.email,
                    "contratado_em": f.contratado_em.isoformat(),
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
                "contratado_em": f.contratado_em.isoformat(),
            }
            for f in getattr(sector, 'funcionarios', [])
        ]
    }
