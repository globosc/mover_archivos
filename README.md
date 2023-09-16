# Script para Mover Archivos que no son Fotos

Este script Python te permite mover archivos que no son fotos a una carpeta específica, que se crea en base a la extensión del archivo. 

## Motivación

Este script nace de la necesidad de organizar mi carpeta de fotos, que a lo largo del tiempo se había llenado de una variedad de archivos de distintos tipos. La situación se volvió confusa y poco práctica, ya que era difícil encontrar las fotos que buscaba entre la maraña de archivos no relacionados.

La idea detrás de este script es simplificar la tarea de limpiar y organizar mi colección de fotos. Permite identificar automáticamente los archivos que no son fotos, basándose en la extensión del archivo, y los mueve a una carpeta separada. Esto hace que sea mucho más fácil mantener organizadas las fotos y eliminar archivos no deseados.

Espero que este script sea útil para otros usuarios que enfrenten problemas similares de organización de archivos y les ayude a mantener sus colecciones de fotos más ordenadas y accesibles.

Si tienes alguna pregunta o sugerencia para mejorar este script, no dudes en ponerte en contacto conmigo o contribuir al proyecto.


## Descripción

A menudo, tenemos una carpeta llena de archivos y queremos organizarla, separando las fotos de otros tipos de archivos. Este script identifica archivos que no son fotos (basados en la extensión del archivo) y los mueve a una carpeta designada.

## Uso

### Requisitos previos

- Python 3.11

### Ejecución

1. Clona o descarga este repositorio en tu computadora.
2. Abre una terminal o línea de comandos.
3. Navega al directorio donde se encuentra el script.
4. Ejecuta el script con el siguiente comando: `python mover_archivos_no_fotos.py`

5. Sigue las instrucciones en la pantalla.

## Configuración Personalizada

Puedes personalizar la configuración del script ajustando las siguientes variables en el código:

- `ruta_base`: La ruta de la carpeta que contiene los archivos a analizar.
- `ruta_carpeta_no_fotos`: La ruta de la carpeta donde se moverán los archivos que no son fotos.
- `archivo_registro`: La ruta del archivo de registro que registra los movimientos realizados.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Clona tu repositorio fork en tu máquina local.
3. Crea una nueva rama para tu contribución: `git checkout -b mi-contribucion`.
4. Realiza tus cambios y commitea: `git commit -m "Añade mi contribución"`.
5. Haz un push de tus cambios: `git push origin mi-contribucion`.
6. Crea una solicitud de extracción en GitHub.


