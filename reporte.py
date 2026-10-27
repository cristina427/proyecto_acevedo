from openpyxl import Workbook


def generar_reporte(
    validos,
    rechazados,
    colisiones
):

    libro = Workbook()

    # Hoja 1 - Carga_Sistema

    hoja_validos = libro.active
    hoja_validos.title = "Carga_Sistema"

    hoja_validos.append([
        "consecutivo",
        "tipo_novedad",
        "tipo_documento",
        "numero_documento",
        "nombre_completo",
        "correo_corporativo",
        "codigo_cargo",
        "nombre_cargo",
        "nivel",
        "centro_costo",
        "area",
        "perfil_sistema",
        "requiere_aprobacion",
        "fecha_efectiva",
        "telefono",
        "fecha_vinculacion_previa"
    ])

    for registro in validos:

        hoja_validos.append([
            registro.get("consecutivo"),
            registro.get("tipo"),
            registro.get("tipo_documento"),
            registro.get("numero_documento"),
            registro.get("nombre_completo"),
            registro.get("correo_corporativo"),
            registro.get("cargo"),
            registro.get("nombre_cargo"),
            registro.get("nivel"),
            registro.get("centro_costo"),
            registro.get("area"),
            registro.get("perfil_sistema"),
            registro.get("requiere_aprobacion"),
            registro.get("fecha_efectiva"),
            registro.get("telefono"),
            registro.get("fecha_vinculacion_previa")
        ])

    # Hoja 2 - Rechazados

    hoja_rechazados = libro.create_sheet(
        "Rechazados"
    )

    hoja_rechazados.append([
        "consecutivo",
        "tipo",
        "numero_documento",
        "nombre",
        "motivo"
    ])

    for registro in rechazados:

        novedad = registro["registro"]

        hoja_rechazados.append([
            novedad.get("consecutivo"),
            novedad.get("tipo"),
            novedad.get("numero_documento"),
            (
                f"{novedad.get('nombres', '')} "
                f"{novedad.get('apellidos', '')}"
            ).strip(),
            "; ".join(
                str(error)
                for error in registro["errores"]
            )
        ])

    # Hoja 3 - Colisiones_Correo

    hoja_colisiones = libro.create_sheet(
        "Colisiones_Correo"
    )

    hoja_colisiones.append([
        "Consecutivo",
        "Base",
        "Correo_Generado"
    ])

    for colision in colisiones:

        hoja_colisiones.append([
            colision["consecutivo"],
            colision["base"],
            colision["correo_generado"]
        ])

    # Hoja 4 - Resumen

    hoja_resumen = libro.create_sheet(
        "Resumen"
    )

    hoja_resumen.append([
        "Concepto",
        "Cantidad"
    ])

    hoja_resumen.append([
        "Validos",
        len(validos)
    ])

    hoja_resumen.append([
        "Rechazados",
        len(rechazados)
    ])

    hoja_resumen.append([
        "Total",
        len(validos) + len(rechazados)
    ])

    libro.save(
        "salida/reporte_novedades.xlsx"
    )