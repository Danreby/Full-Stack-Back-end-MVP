from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from model.funcionario import Funcionario

class FuncionarioSchema(BaseModel):
    """Define como um novo funcionário a ser inserido deve ser representado."""
    name: str = Field(..., example="João Silva")
    email: str = Field(..., example="joao.silva@example.com")
    sector_id: int = Field(..., example=1)

class FuncionarioBuscaSchema(BaseModel):
    """Define como a busca de funcionário deve ser representada (por ID)."""
    id: int = 1

# funcionario.py
class FuncionarioViewSchema(BaseModel):
    id: int
    name: str
    email: str
    sector: Optional[dict] = None

class FuncionarioPathSchema(BaseModel):
    id: int

class ListagemFuncionariosSchema(BaseModel):
    """Define como a listagem de funcionários será retornada."""
    funcionarios: List[FuncionarioViewSchema]

class FuncionarioDelSchema(BaseModel):
    """Define como é a resposta de uma remoção de funcionário."""
    message: str
    id: int


def apresenta_funcionarios(funcionarios: List[Funcionario]):
    """Retorna uma representação de vários funcionários seguindo ListagemFuncionariosSchema."""
    result = []
    for f in funcionarios:
        result.append({
            "id": f.pk_funcionario if hasattr(f, 'pk_funcionario') else f.id,
            "name": f.name,
            "email": f.email,
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
        "sector": {
            "id": funcionario.sector.pk_sector if hasattr(funcionario.sector, 'pk_sector') else funcionario.sector.id,
            "name": funcionario.sector.name,
        }
    }

def apresenta_funcionario_deletado(funcionario: Funcionario):
    """Retorna mensagem de confirmação de remoção de um funcionário."""
    return {
        "message": f"Funcionário '{funcionario.name}' removido com sucesso.",
        "id": funcionario.pk_funcionario if hasattr(funcionario, 'pk_funcionario') else funcionario.id
    }

def apresenta_funcionario_atualizado(funcionario: Funcionario):
    """Retorna uma representação do funcionário atualizado."""
    return apresenta_funcionario(funcionario)
