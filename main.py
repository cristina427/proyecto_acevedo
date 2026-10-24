from modulos.configuracion import cargar_configuracion
from modulos.lectura import obtener_json_reciente
from modulos.validacion import validar_modulo
from modulos.validacion import validar_tipo_novedad

parametros, campos_obligatorios = cargar_configuracion()

novedades = obtener_json_reciente()

print(f"Total novedades: {len(novedades)}")

validar_modulo()

for novedad in novedades:

    tipo = novedad["tipo"].strip().upper()

    requeridos = campos_obligatorios[tipo]

    print(requeridos)
for campo in requeridos:
    print(campo) 