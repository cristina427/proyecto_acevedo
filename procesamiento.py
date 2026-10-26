from modulos.validacion import (validar_documento, validar_telefono, limpiar_telefono, validar_fecha)

def procesar_novedades(novedades, campos_obligatorios, centros_costo, cargos, matriz_roles, parametros):

    validos = []
    rechazados = []

    for novedad in novedades:

        tipo = novedad.get("tipo","").strip().upper()

        requeridos = campos_obligatorios.get(tipo,[])

        errores = []

        # Validar campos obligatorios

        for campo in requeridos:

            valor = novedad.get(campo)

            if valor in [None, ""]: errores.append(f"Falta el campo {campo}")

        # Validar documento

        tipo_doc = novedad.get("tipo_documento","")

        numero_doc = novedad.get("numero_documento","")
        telefono = novedad.get("telefono","")

        if telefono:

         if not validar_telefono(telefono):

          errores.append("Telefono invalido")

        fecha_efectiva = novedad.get("fecha_efectiva", "")

        if fecha_efectiva:
          dias_maximos = int(parametros["dias_maximo_futuro"])

        if not validar_fecha(fecha_efectiva, dias_maximos):
           errores.append("Fecha invalida")

        if tipo_doc and numero_doc:

            if not validar_documento(tipo_doc, numero_doc):
                errores.append("Documento invalido")

        # Validar centro de costo

        centro = novedad.get("centro_costo")

        if centro and centro not in centros_costo:

            errores.append("Centro de costo invalido")

        # Validar cargo

        cargo = novedad.get("cargo")

        if cargo and cargo not in cargos:

            errores.append("Cargo invalido")
        if (cargo in cargos and centro in centros_costo):

         area_cargo = (cargos[cargo]["area"])

         area_centro = (centros_costo[centro]["area"])

        if area_cargo != area_centro:

         errores.append(
            f"Area inconsistente: "
            f"{area_cargo} != "
            f"{area_centro}") 

        # Clasificación
       
        if errores:

            rechazados.append({"registro": novedad, "errores": errores})

        else:

            cargo = novedad.get("cargo")

            area_centro = (centros_costo[centro]["area"])

            clave_rol = (f"{cargo}|{area_centro}")


        rol = matriz_roles.get(clave_rol)

        if rol is None:

         errores.append("Combinacion cargo-area inexistente")

         rechazados.append({"registro": novedad, "errores": errores})

        continue

    novedad["perfil_sistema"] = (rol["perfil"])

    novedad["requiere_aprobacion"] = (
    rol["requiere_aprobacion"])

    dominio = "empresa.com"

    correo = (
                f"{novedad['nombres'].lower()}."
                f"{novedad['apellidos'].lower()}"
                f"@{dominio}"
            )

    correo = correo.replace(" ", "")

    novedad["correo_corporativo"] = correo

    novedad["telefono"] = (limpiar_telefono(novedad.get("telefono", "")))

    validos.append(novedad)

    return validos, rechazados