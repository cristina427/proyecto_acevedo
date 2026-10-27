import re

from datetime import datetime, timedelta

PATRONES = {
    "centro_costo": re.compile(r"^CC-\d{4}$"),

    "telefono": re.compile(r"\d"),

    "correo": re.compile(
        r"^[a-z]+(?:\.[a-z]+)?@[a-z0-9.-]+\.[a-z]{2,}$"
    ),

    "documento_cc": re.compile(
        r"^\d{6,10}$"
    ),

    "documento_ce": re.compile(
        r"^(?:[A-Za-z]\d{6,9}|\d{6,10})$"
    ),

    "documento_pa": re.compile(
        r"^(?=.*[A-Za-z])[A-Za-z0-9]{6,12}$"
    ),

    "fechas_observaciones": re.compile(
    r"\b(?:\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})\b"
)
}


def validar_modulo():
    print("Modulo de validaciones cargado")


def validar_centro_costo(centro_costo):

    return (
        PATRONES["centro_costo"]
        .match(centro_costo)
        is not None
    )


def limpiar_telefono(telefono):

    digitos = "".join(
        PATRONES["telefono"].findall(
            str(telefono)
        )
    )

    return digitos


def validar_telefono(telefono):

    digitos = limpiar_telefono(
        telefono
    )

    return len(digitos) == 10


def validar_documento(
    tipo_documento,
    numero_documento
):

    numero = (
        str(numero_documento)
        .replace(".", "")
        .replace("-", "")
        .replace(" ", "")
    )

    tipo = tipo_documento.upper()

    if tipo == "CC":
        return (
            PATRONES["documento_cc"]
            .match(numero)
            is not None
        )

    if tipo == "CE":
        return (
            PATRONES["documento_ce"]
            .match(numero)
            is not None
        )

    if tipo == "PA":
        return (
            PATRONES["documento_pa"]
            .match(numero)
            is not None
        )

    return False


def validar_tipo_novedad(tipo):

    tipos_validos = [
        "ALTA",
        "CAMBIO_CARGO",
        "TRASLADO",
        "RETIRO"
    ]

    return (
        tipo.strip().upper()
        in tipos_validos
    )
def validar_fecha(
    fecha_texto,
    dias_maximo_futuro
):

    formatos = [
        "%d/%m/%Y",
        "%Y-%m-%d"
    ]

    fecha = None

    for formato in formatos:

        try:

            fecha = datetime.strptime(
                fecha_texto,
                formato
            )

            break

        except ValueError:
            pass

    if fecha is None:
        return False

    hoy = datetime.now()

    fecha_solo = fecha.date()

    hoy_solo = hoy.date()

    limite = (
        hoy_solo
        + timedelta(
            days=dias_maximo_futuro
        )
    )

    if fecha_solo < hoy_solo:
        return False

    if fecha_solo > limite:
        return False

    return True

def extraer_fecha_mas_antigua(
    observaciones
):

    if not observaciones:

        return ""

    textos_fechas = (
        PATRONES[
            "fechas_observaciones"
        ].findall(
            observaciones
        )
    )

    fechas = []

    formatos = [
        "%d/%m/%Y",
        "%Y-%m-%d"
    ]

    for texto_fecha in textos_fechas:

        for formato in formatos:

            try:

                fecha = datetime.strptime(
                    texto_fecha,
                    formato
                )

                fechas.append(
                    fecha
                )

                break

            except ValueError:

                pass

    if not fechas:

        return ""

    fecha_mas_antigua = min(
        fechas
    )

    return fecha_mas_antigua.strftime(
        "%Y-%m-%d"
    )