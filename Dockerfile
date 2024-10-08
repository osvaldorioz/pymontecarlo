# Usa una imagen base con Python 3.12
FROM python:3.12-slim

# Instala las dependencias necesarias para compilar C++
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    g++ \
    python3-dev \
    && apt-get clean

# Instalar PyBind11
RUN pip install pybind11

# Copia el código fuente
COPY . /app
WORKDIR /app

# Compilar el código C++ y Python con PyBind11
RUN c++ -Ofast -Wall -shared -std=c++20 -fPIC $(python3.12 -m pybind11 --includes) app/pi_montecarlo.cpp -o pi_montecarlo$(python3.12-config --extension-suffix)

# Instalar cualquier otra dependencia Python
RUN pip install -r requirements.txt

# Exponer el puerto de la aplicación (por ejemplo, 8000 para FastAPI)
EXPOSE 8000

# Comando para ejecutar el microservicio
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


