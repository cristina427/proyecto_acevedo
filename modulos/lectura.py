import os
import json
from modulos.excepciones import ErrorArchivoEntrada

def obtener_json_reciente():

    archivos = [
    archivo
    for archivo in os.listdir("entrada")
    if archivo.endswith(".json")
]
    if not archivos:
     raise ErrorArchivoEntrada(
        "No existen archivos JSON en la carpeta entrada"
    )

    archivo = archivos[0]

    print(f"Archivo encontrado: {archivo}")
    ruta = os.path.join("entrada", archivo)

    with open(ruta, "r", encoding="utf-8") as archivo_json:
     datos = json.load(archivo_json)

    novedades = datos["novedades"]

    return novedades

