# 🧠 FastAPI - Trabajo Práctico Integrador

El objetivo fue construir una API mínima en **FastAPI**, contenerizarla con **Docker**, integrarla con una base de datos y automatizar su testeo mediante **GitHub Actions**.

---

## Características

- API REST con FastAPI (Python)
- Endpoints:
  - `GET /health` → Verifica el estado del servicio
  - `GET /products/` → Lista los productos registrados
  - `POST /products/` → Crea un nuevo producto
- Validaciones automáticas de campos con Pydantic
- Persistencia de datos con SQLite / PostgreSQL
- Pruebas automáticas con `pytest`
- Integración continua con GitHub Actions

---

##  Estructura del proyecto
```txt
fastapi-tp/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── database.py
├── tests/
│   ├── test_api.py
│   └── test_validations.py
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env
├── requirements.txt
└── README.md

##  Requisitos previos

- Tener instalado **Docker** y **Docker Compose**.
- No es necesario tener Python instalado localmente.

---

##  Ejecución del proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/mevaktecno-vane/fastapi-tp.git
   cd fastapi-tp

2. Crear un archivo .env en la raíz con el siguiente contenido:
DATABASE_URL=sqlite:///./test.db

3. Construir y ejecutar los contenedores:
docker compose up --build

4. Acceder a la API:

API principal: http://localhost:8000

Documentación interactiva (Swagger): http://localhost:8000/docs

Ejecutar los tests

Si querés correr los tests localmente (sin Docker):
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -v

Variables de entorno
DATABASE_URL	URL de conexión a la base de datos	sqlite:///./test.db

Docker Compose

Ejemplo del servicio:
services:
  api:
    build: .
    ports:
      - "8000:8000"
    env_file: .env
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: products
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password

Integración continua (GitHub Actions)

Este proyecto incluye un flujo CI que:

-Instala dependencias.

-Ejecuta los tests con pytest.

-Verifica que la build del contenedor sea exitosa.

El archivo se encuentra en:
 .github/workflows/ci.yml.

Evidencias de ejecución

Capturas recomendadas: se incluyen capturas y explicaciones del proceso en un archivo PDF

1- Tests pytest -v pasando 

2- Ejecución de docker compose up mostrando el contenedor FastAPI iniciado

3- Documentación /docs accesible

4- Resultado del pipeline en GitHub Actions

Materia: Prácticas Profesionalizantes 1

Mara Vanesa San Martín
Estudiante DevOps 1er año
2025
