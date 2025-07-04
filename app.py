from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request, jsonify
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError

# ✅ import do engine, Base e SessionLocal (renomeado para Session aqui)
from model.base import Base, engine, SessionLocal as Session
from model.funcionario import Funcionario
from model.sectors import Sector

# seus schemas e funções de apresentação
from schemas import (
    FuncionarioSchema,
    FuncionarioViewSchema,
    ListagemFuncionariosSchema,
    FuncionarioDelSchema,
    apresenta_funcionarios,
    apresenta_funcionario,

    SectorSchema,
    SectorViewSchema,
    ListagemSectorsSchema,
    apresenta_sectors,
    apresenta_sector,

    ErrorSchema,
)
# ——— cria o banco e as tabelas se ainda não existirem ———
Base.metadata.create_all(bind=engine)

# ——— inicia a API ———
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Tags para documentação
home_tag        = Tag(name="Documentação",   description="Seleção de UI: Swagger, Redoc ou RapiDoc")
sector_tag      = Tag(name="Sector",         description="CRUD de setores")
funcionario_tag = Tag(name="Funcionario",    description="CRUD de funcionários")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para a interface OpenAPI."""
    return redirect('/openapi')


# ==== ROTAS DE SECTOR ====

@app.post(
    '/sectors',
    tags=[sector_tag],
    responses={"200": SectorViewSchema, "409": ErrorSchema, "400": ErrorSchema}
)
def add_sector(form: SectorSchema):
    """Adiciona um novo setor à base."""
    session = Session()
    sector = Sector(name=form.name)
    try:
        session.add(sector)
        session.commit()
        return apresenta_sector(sector), 200

    except IntegrityError:
        session.rollback()
        return {"message": "Setor com esse nome já existe."}, 409

    except Exception:
        session.rollback()
        return {"message": "Não foi possível salvar o setor."}, 400


@app.get(
    '/sectors',
    tags=[sector_tag],
    responses={"200": ListagemSectorsSchema, "404": ErrorSchema}
)
def get_sectors():
    """Retorna todos os setores cadastrados."""
    session = Session()
    sectors = session.query(Sector).all()
    return apresenta_sectors(sectors), 200


# ==== ROTAS DE FUNCIONARIO ====

@app.post(
    '/funcionarios',
    tags=[funcionario_tag],
    responses={"200": FuncionarioViewSchema, "409": ErrorSchema, "400": ErrorSchema}
)
def add_funcionario(form: FuncionarioSchema):
    """Adiciona um novo funcionário, referenciando um setor existente."""
    session = Session()
    try:
        funcionario = Funcionario(
            name=form.name,
            email=form.email,
            sector_id=form.sector_id
        )
        session.add(funcionario)
        session.commit()
        return apresenta_funcionario(funcionario), 200

    except IntegrityError:
        session.rollback()
        return {"message": "Erro de integridade (verifique sector_id)."}, 409

    except Exception:
        session.rollback()
        return {"message": "Não foi possível salvar o funcionário."}, 400


@app.get(
    '/funcionarios',
    tags=[funcionario_tag],
    responses={"200": ListagemFuncionariosSchema, "404": ErrorSchema}
)
def get_funcionarios():
    """Retorna todos os funcionários com o setor aninhado."""
    session = Session()
    funcionarios = session.query(Funcionario).all()
    return apresenta_funcionarios(funcionarios), 200


if __name__ == '__main__':
    # sobe o servidor em 0.0.0.0:8000
    app.run("0.0.0.0", port=8000, debug=True)
