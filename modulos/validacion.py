import re

PATRONES = {
    "centro_costo": re.compile(r"^CC-\d{4}$"),
    "telefono": re.compile(r"\d"),
    "correo": re.compile(
        r"^[a-z]+(?:\.[a-z]+)?@[a-z0-9.-]+\.[a-z]{2,}$"
    ),
}


def validar_modulo():
    print("Modulo de validaciones cargado")


def validar_centro_costo(centro_costo):

    if PATRONES["centro_costo"].match(centro_costo):
        return True

    return False
def limpiar_telefono(telefono):

    digitos = "".join(
        PATRONES["telefono"].findall(telefono)
    )

    return digitos

def validar_tipo_novedad(tipo):

    tipos_validos = [
        "ALTA",
        "CAMBIO_CARGO",
        "TRASLADO",
        "RETIRO"
    ]

    tipo = tipo.strip().upper()

    return tipo in tipos_validos