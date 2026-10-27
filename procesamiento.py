import unicodedata

from modulos.validacion import (
    validar_documento,
    validar_telefono,
    limpiar_telefono,
    validar_fecha
)


def procesar_novedades(
    novedades,
    campos_obligatorios,
    centros_costo,
    cargos,
    matriz_roles,
    parametros
):

    validos = []
    rechazados = []
    colisiones = []

    correos_asignados = {}

    for novedad in novedades:

        tipo = novedad.get(
            "tipo",
            ""
        ).strip().upper()

        requeridos = campos_obligatorios.get(
            tipo,
            []
        )

        errores = []

        # Campos obligatorios
        for campo in requeridos:

            valor = novedad.get(campo)

            if valor in [None, ""]:
                errores.append(
                    f"Falta el campo {campo}"
                )

        # Documento
        tipo_doc = novedad.get(
            "tipo_documento",
            ""
        )

        numero_doc = novedad.get(
            "numero_documento",
            ""
        )

        if tipo_doc and numero_doc:

            if not validar_documento(
                tipo_doc,
                numero_doc
            ):

                errores.append(
                    "Documento invalido"
                )

        # Telefono
        telefono = novedad.get(
            "telefono",
            ""
        )

        if telefono:

            if not validar_telefono(
                telefono
            ):

                errores.append(
                    "Telefono invalido"
                )

        # Fecha
        fecha_efectiva = novedad.get(
            "fecha_efectiva",
            ""
        )

        if fecha_efectiva:

            dias_maximos = int(
                parametros[
                    "dias_maximo_futuro"
                ]
            )

            if not validar_fecha(
                fecha_efectiva,
                dias_maximos
            ):

                errores.append(
                    "Fecha invalida"
                )

        # Centro de costo
        centro = novedad.get(
            "centro_costo"
        )

        if centro and centro not in centros_costo:

            errores.append(
                "Centro de costo invalido"
            )

        # Cargo
        cargo = novedad.get(
            "cargo"
        )

        if cargo and cargo not in cargos:

            errores.append(
                "Cargo invalido"
            )

        # Validacion cruzada de areas
        if (
            cargo in cargos
            and centro in centros_costo
        ):

            area_cargo = (
                cargos[cargo]["area"]
            )

            area_centro = (
                centros_costo[centro]["area"]
            )

            if area_cargo != area_centro:

                errores.append(
                    f"Area inconsistente: "
                    f"{area_cargo} != "
                    f"{area_centro}"
                )

        # Rechazados
        if errores:

            rechazados.append(
                {
                    "registro": novedad,
                    "errores": errores
                }
            )

            continue

        # Perfil
        area_centro = (
            centros_costo[centro]["area"]
        )

        clave_rol = (
            f"{cargo}|{area_centro}"
        )

        rol = matriz_roles.get(
            clave_rol
        )

        if rol is None:

            rechazados.append(
                {
                    "registro": novedad,
                    "errores": [
                        "Combinacion cargo-area inexistente"
                    ]
                }
            )

            continue

        novedad["perfil_sistema"] = (
            rol["perfil"]
        )

        novedad["requiere_aprobacion"] = (
            rol["requiere_aprobacion"]
        )

        # Correo corporativo
        dominio = parametros[
            "dominio_correo"
        ]

        primer_nombre = (
            novedad["nombres"]
            .strip()
            .split()[0]
        )

        primer_apellido = (
            novedad["apellidos"]
            .strip()
            .split()[0]
        )

        base = (
            f"{primer_nombre}.{primer_apellido}"
        ).lower()

        base = "".join(
            c
            for c in unicodedata.normalize(
                "NFD",
                base
            )
            if unicodedata.category(c)
            != "Mn"
        )

        base = base.replace(
            "ñ",
            "n"
        )

        base = "".join(
            c
            for c in base
            if c.isalpha() or c == "."
        )

        cantidad = correos_asignados.get(
            base,
            0
        )

        correos_asignados[base] = (
            cantidad + 1
        )

        if cantidad == 0:

            correo = (
                f"{base}@{dominio}"
            )

        else:

            correo = (
                f"{base}{cantidad + 1}@{dominio}"
            )

            colisiones.append(
                {
                    "consecutivo": novedad.get(
                        "consecutivo"
                    ),
                    "base": base,
                    "correo_generado": correo
                }
            )

        novedad[
            "correo_corporativo"
        ] = correo

        # Telefono normalizado
        novedad["telefono"] = (
            limpiar_telefono(
                novedad.get(
                    "telefono",
                    ""
                )
            )
        )

        validos.append(
            novedad
        )

    return (
        validos,
        rechazados,
        colisiones
    )