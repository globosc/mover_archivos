import os
import shutil
from tqdm import tqdm
from pathlib import Path

# Ruta de la carpeta que contiene los archivos
ruta_base = Path(r"D:\photos")  # Reemplaza con la ruta de tu carpeta

# Ruta de la carpeta donde se moverán los archivos que no son fotos
ruta_carpeta_no_fotos = Path(r"D:\photos\archivos")  # Cambia la ruta según sea necesario

# Ruta del archivo de registro
archivo_registro = Path("archivos_movidos.txt")

# Lista de extensiones de archivo válidas para fotos
extensiones_validas = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

def mover_archivos_no_fotos(ruta_base, ruta_destino, archivo_registro):
    ruta_base = Path(ruta_base)
    ruta_destino = Path(ruta_destino)

    # Verifica si la carpeta de destino ya existe
    if ruta_destino.exists() and not ruta_destino.is_dir():
        raise ValueError("La carpeta de destino no es una carpeta válida.")

    # Crea la carpeta de destino si no existe
    ruta_destino.mkdir(parents=True, exist_ok=True)

    archivos_movidos = set()
    archivos_contados = 0  # Inicializa el contador de archivos movidos

    # Obtiene la lista de archivos para mostrar una barra de progreso
    archivos_a_procesar = list(ruta_base.rglob('*'))

    for ruta_archivo in tqdm(archivos_a_procesar, desc="Moviendo archivos"):
        if ruta_archivo.is_file():
            extension = ruta_archivo.suffix.lower()
            
            # Verifica si la extensión del archivo es una extensión válida para fotos
            if extension not in extensiones_validas:
                # Genera un nuevo nombre de archivo único en caso de colisión
                nuevo_nombre = obtener_nombre_unico(ruta_destino, ruta_archivo.name)
                
                # Ruta de destino del archivo no foto
                ruta_destino_archivo = ruta_destino / nuevo_nombre
                
                # Mueve el archivo a la carpeta de no fotos
                shutil.move(str(ruta_archivo), str(ruta_destino_archivo))
                
                # Registra el movimiento en el archivo de registro
                registrar_movimiento(archivo_registro, ruta_archivo, ruta_destino_archivo)
                
                # Agrega el archivo movido al conjunto de archivos movidos
                archivos_movidos.add(ruta_archivo)
                
                archivos_contados += 1  # Incrementa el contador de archivos movidos

    # Guarda la lista de archivos movidos en un archivo de registro
    guardar_archivos_movidos(archivo_registro, archivos_movidos)

    # Muestra el total de archivos movidos
    print(f"Total de archivos movidos: {archivos_contados}")

def obtener_nombre_unico(ruta_destino, nombre_original):
    nombre_base, extension = os.path.splitext(nombre_original)
    
    nuevo_nombre = nombre_original
    contador = 1
    
    while (ruta_destino / nuevo_nombre).exists():
        nuevo_nombre = f"{nombre_base}_{contador}{extension}"
        contador += 1

    return nuevo_nombre

def registrar_movimiento(archivo_registro, ruta_origen, ruta_destino):
    with open(archivo_registro, 'a', encoding='utf-8') as registro:
        registro.write(f"Moved: {ruta_origen} -> {ruta_destino}\n")

def guardar_archivos_movidos(archivo_registro, archivos_movidos):
    with open(archivo_registro, 'a', encoding='utf-8') as registro:
        for ruta_archivo in archivos_movidos:
            registro.write(f"Processed: {ruta_archivo}\n")

if __name__ == "__main__":
    mover_archivos_no_fotos(ruta_base, ruta_carpeta_no_fotos, archivo_registro)
