from openpyxl import Workbook


def generar_reporte(validos, rechazados):

    libro = Workbook()

    hoja_validos = libro.active
    hoja_validos.title = "Carga_Sistema"

    hoja_rechazados = libro.create_sheet("Rechazados")

    hoja_validos.append(
        ["Consecutivo", "Tipo", "Perfil"])

    for registro in validos:

        hoja_validos.append([registro.get("consecutivo"), registro.get("tipo"), registro.get("perfil_sistema")])

    hoja_rechazados.append(["Errores"])

    for registro in rechazados: hoja_rechazados.append([ "; ".join(registro["errores"])])

    libro.save("salida/reporte_novedades.xlsx")