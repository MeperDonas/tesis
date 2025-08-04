# 1. Base image: Python ligero
FROM python:3.11-slim

# 2. Configuración de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Directorio de trabajo
WORKDIR /app

# 4. Instalación de dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# 5. Copia de requirements y pip install
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 6. Copia del código de la aplicación
COPY . .

# 7. No recolectar estáticos en build para maximizar cache; se hará en runtime

# 8. Exponer puerto de Gunicorn
EXPOSE 8000

# 9. Comando por defecto
CMD ["gunicorn", "thesis.wsgi:application", "--bind", "0.0.0.0:8000"]