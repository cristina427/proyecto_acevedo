from datetime import datetime
from openpyxl import Workbook
import os

eventos = []


def registrar_evento(
    nivel,
    modulo,
    funcion,
    mensaje,
    registro="",
    detalle=""
):

    eventos.append({
        "fecha_hora": datetime.now(),
        "nivel": nivel,
        "modulo": modulo,
        "funcion": funcion,
        "registro": registro,
        "mensaje": mensaje,
        "detalle": detalle
    })


def guardar_log():

    os.makedirs(
        "logs",
        exist_ok=True
    )

    libro = Workbook()

    hoja = libro.active

    hoja.title = "Detalle"

    hoja.append([
        "Fecha_Hora",
        "Nivel",
        "Modulo",
        "Funcion",
        "Registro",
        "Mensaje",
        "Detalle"
    ])

    for evento in eventos:

        hoja.append([
            evento["fecha_hora"].strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            evento["nivel"],
            evento["modulo"],
            evento["funcion"],
            evento["registro"],
            evento["mensaje"],
            evento["detalle"]
        ])

    nombre_log = (
        f"log_ejecucion_"
        f"{datetime.now():%Y%m%d_%H%M%S}.xlsx"
    )

    ruta_log = os.path.join(
        "logs",
        nombre_log
    )

    libro.save(ruta_log)