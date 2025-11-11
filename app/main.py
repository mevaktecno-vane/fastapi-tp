from fastapi import FastAPI
from app.routes import products
from app import models, database

# Crea las tablas en la base de datos
models.Base.metadata.create_all(bind=database.engine)

# Inicializa la app
app = FastAPI()

# Endpoint de verificación de estado


@app.get("/health")
def health_check():
    return {"status": "ok"}


# Incluye las rutas de productos
app.include_router(products.router)
