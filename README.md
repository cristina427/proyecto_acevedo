Proyecto Acevedo
Sistema de procesamiento de novedades de personal desarrollado en Python.

Descripción
Este proyecto permite leer un archivo JSON con novedades de personal, validar la información utilizando parámetros almacenados en un archivo Excel, aplicar reglas de negocio y generar un archivo de salida listo para ser consumido por un proceso de automatización.

También genera archivos de log para registrar los eventos ocurridos durante cada ejecución.

Funcionalidades
Lectura de configuración desde Excel.
Lectura de novedades desde JSON.
Validación de documentos.
Validación de teléfonos.
Validación de fechas.
Validación de centros de costo.
Validación de cargos.
Validación cruzada de áreas.
Asignación de perfiles del sistema.
Generación de correos corporativos.
Manejo de colisiones de correo.
Extracción de fechas desde observaciones.
Generación de reportes Excel.
Generación de logs.
Manejo de excepciones personalizadas.
Estructura del proyecto
proyecto_acevedo/
│
├── config/
│   └── parametros.xlsx
│
├── entrada/
│   └── novedades_20261023.json
│
├── logs/
│
├── modulos/
│   ├── configuracion.py
│   ├── lectura.py
│   ├── validacion.py
│   ├── procesamiento.py
│   ├── reporte.py
│   ├── registro.py
│   └── excepciones.py
│
├── salida/
│
├── main.py
└── README.md
Requisitos
Python 3.12 o superior
openpyxl
Instalación:

pip install openpyxl
Ejecución
Ubique el archivo JSON dentro de la carpeta:

entrada/
Ejecute:

python main.py
Los resultados se generan en:

salida/
y los logs en:

logs/
Archivo de configuración
El archivo:

config/parametros.xlsx
contiene cinco hojas:

Parametros
Cargos
Centros_Costo
Matriz_Roles
Campos_Obligatorios
Desde este archivo se controlan las reglas del sistema sin necesidad de modificar el código.

Validaciones implementadas
Tipo de novedad.
Campos obligatorios por tipo.
Documento de identidad.
Fecha efectiva.
Centro de costo.
Cargo.
Teléfono.
Validación cruzada de áreas.
Reglas de negocio
Generación de correo corporativo.
Resolución de colisiones de correo.
Asignación de perfil del sistema.
Validación de correspondencia entre cargo y área.
Extracción de fecha de vinculación previa desde observaciones.
Manejo de excepciones
El proyecto incluye excepciones personalizadas para:

ErrorConfiguracion
ErrorArchivoEntrada
RegistroInvalido
ErrorReglaNegocio
ErrorEscritura
Archivos generados
Reporte
salida/reporte_novedades.xlsx
Contiene las hojas:

Carga_Sistema
Rechazados
Colisiones_Correo
Resumen
Logs
logs/log_ejecucion_.xlsx
Contienen el detalle de cada ejecución.

Evidencia de ejecución
Prueba exitosa:

text Validos: 1 Rechazados: 0 Repote generado correctamente


Prueba con rechazo:


Validos: 0
Rechazados:1
Reporte generado correctamente


---

## Posibles mejoras

- Aplicar formato avanzado a los reportes Excel.
- Mejorar el resumen estadístico
- Incorporar más validaciones.
- Implementar interfaz gráfica
