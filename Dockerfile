FROM python:3.10-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
# Imagen base
FROM python:3.10-slim

# Carpeta de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto (Render usa variable PORT)
EXPOSE 5000

# Comando para iniciar la app
CMD ["python", "app.py"]
