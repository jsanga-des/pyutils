import os
from typing import List
from .verificar_carpeta_existe import verificar_carpeta_existe

def obtener_archivos_por_extension(ruta_carpeta: str, extension: str) -> List[str]:
    """
    Obtiene todos los archivos con una extensión específica de una carpeta.

    Args:
        ruta_carpeta (str): Ruta de la carpeta
        extension (str): Extensión a buscar (ej: '.xsig', '.xml')

    Returns:
        List[str]: Lista de rutas completas de archivos encontrados
    """
    if not verificar_carpeta_existe(ruta_carpeta):
        return []

    return [
        os.path.join(ruta_carpeta, archivo)
        for archivo in os.listdir(ruta_carpeta)
        if archivo.lower().endswith(extension.lower())
    ]
