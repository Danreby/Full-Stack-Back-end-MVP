# 🚀 MVP Full Stack — API e Front-end

Este é um projeto **Full Stack** simples que integra **Flask** (Python) no back-end com um front-end em **HTML, CSS e JavaScript puro**.

O objetivo é demonstrar de forma prática conceitos de desenvolvimento Full Stack, incluindo:

- **CRUD de Funcionários e Setores**
- Consumo de **API REST**
- Manipulação dinâmica de interface no Front-end

---

## 📂 Tecnologias Utilizadas

- **Back-end:** Flask + Flask-OpenAPI3 + SQLAlchemy + SQLite
- **Front-end:** HTML5, CSS3, JavaScript (Fetch API)
- **Documentação da API:** Swagger / Redoc (acessível através da própria API)

---

## ⚙️ Como Executar o Projeto

### 1. Pré-requisitos

- Python 3.8 ou superior
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (opcional, porém recomendado)

---

### 2. Configuração do Ambiente Virtual

No terminal, execute os comandos abaixo:

```bash
# Crie o ambiente virtual
python -m venv env

# Ative o ambiente virtual (Windows)
.\env\Scripts\activate

# Instalando dependencias
pip install -r requirements.txt

#rodando o servidor
flask run --host 0.0.0.0 --port 5000
