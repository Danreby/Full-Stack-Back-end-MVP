from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from model.funcionario import Funcionario

# ─── CREATE ─────────────────────────────────────────────────────────

class FuncionarioSchema(BaseModel):
    """Define como um novo funcionário a ser inserido deve ser representado."""
    name: str = "João Silva"
    email: str = "joao.silva@example.com"
    sector_id: int = 1
    contratado_em: Optional[datetime] = None  # permite informar a data de contratação

# ─── READ (single) ───────────────────────────────────────────────────

class FuncionarioBuscaSchema(BaseModel):
    """Define como a busca de funcionário deve ser representada (por ID)."""
    id: int = 1

# funcionario.py
class FuncionarioViewSchema(BaseModel):
    id: int
    name: str
    email: str
    contratado_em: datetime
    sector: Optional[dict] = None


# ─── READ (list) ─────────────────────────────────────────────────────

class ListagemFuncionariosSchema(BaseModel):
    """Define como a listagem de funcionários será retornada."""
    funcionarios: List[FuncionarioViewSchema]

# ─── DELETE ──────────────────────────────────────────────────────────

class FuncionarioDelSchema(BaseModel):
    """Define como é a resposta de uma remoção de funcionário."""
    message: str
    id: int

# ─── FUNÇÕES DE APRESENTAÇÃO ─────────────────────────────────────────

def apresenta_funcionarios(funcionarios: List[Funcionario]):
    """Retorna uma representação de vários funcionários seguindo ListagemFuncionariosSchema."""
    result = []
    for f in funcionarios:
        result.append({
            "id": f.pk_funcionario if hasattr(f, 'pk_funcionario') else f.id,
            "name": f.name,
            "email": f.email,
            "contratado_em": f.contratado_em.isoformat(),
            "sector": {
                "id": f.sector.pk_sector if hasattr(f.sector, 'pk_sector') else f.sector.id,
                "name": f.sector.name,
            }
        })
    return {"funcionarios": result}

def apresenta_funcionario(funcionario: Funcionario):
    """Retorna uma representação de um funcionário seguindo FuncionarioViewSchema."""
    return {
        "id": funcionario.pk_funcionario if hasattr(funcionario, 'pk_funcionario') else funcionario.id,
        "name": funcionario.name,
        "email": funcionario.email,
        "contratado_em": funcionario.contratado_em.isoformat(),
        "sector": {
            "id": funcionario.sector.pk_sector if hasattr(funcionario.sector, 'pk_sector') else funcionario.sector.id,
            "name": funcionario.sector.name,
        }
    }
