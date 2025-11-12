# Etapa 1: construcción
FROM python:3.11-slim AS builder

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends build-essential

# Copiar archivos de dependencias primero (para aprovechar cache)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 2: imagen final (más liviana)
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias ya instaladas
COPY --from=builder /usr/local /usr/local

# Copiar código fuente
COPY . .

# Exponer el puerto (FastAPI por defecto usa 8000)
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
