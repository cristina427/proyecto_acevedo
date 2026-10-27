from modulos.configuracion import cargar_configuracion
from modulos.lectura import obtener_json_reciente
from modulos.validacion import validar_modulo
from modulos.procesamiento import procesar_novedades
from modulos.reporte import generar_reporte
from modulos.registro import guardar_log
from modulos.excepciones import (
    ErrorConfiguracion,
    ErrorArchivoEntrada,
    ErrorEscritura
)

try:

    (parametros,
     campos_obligatorios,
     centros_costo,
     cargos,
     matriz_roles) = cargar_configuracion()

    novedades = obtener_json_reciente()

    validar_modulo()

    validos, rechazados, colisiones = (
        procesar_novedades(
            novedades,
            campos_obligatorios,
            centros_costo,
            cargos,
            matriz_roles,
            parametros
        )
    )

    print(f"Validos: {len(validos)}")
    print(f"Rechazados: {len(rechazados)}")

    generar_reporte(
        validos,
        rechazados,
        colisiones
    )

    guardar_log()

    print(
        "Reporte generado correctamente"
    )

except ErrorConfiguracion as e:

    print(
        f"Error de configuracion: {e}"
    )

except ErrorArchivoEntrada as e:

    print(
        f"Error de entrada: {e}"
    )

except ErrorEscritura as e:

    print(
        f"Error de escritura: {e}"
    )

except Exception as e:

    print(
        f"Error inesperado: {e}"
    )

