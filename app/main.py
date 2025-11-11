from fastapi import FastAPI
from app.database import engine, Base

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}
