
# main.py
from fastapi import FastAPI

# Crear la instancia de la aplicación
app = FastAPI(
title="Mi Primera API",
description="API de ejemplo para SENA",
version="1.0.0",
)


# Definir un endpoint
@app.get("/")
def raiz():
    """Endpoint raíz que retorna un saludo"""
    return {"mensaje": "Hola desde FastAPI"}

   
   
    # Endpoint con condición
@app.get("/saludar/{nombre}")
def saludar(nombre: str):
    """Endpoint que saluda según el nombre recibido"""

    if nombre.lower() == "jhojan":
        return {"mensaje": "¡Hola Jhojan, bienvenido!"}
    elif nombre.lower() == "sena":
        return {"mensaje": "Saludos a la comunidad SENA!"}
    else:
        return {"mensaje": f"Hola, {nombre}!"}

