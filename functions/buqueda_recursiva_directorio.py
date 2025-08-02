import os
from typing import List, Optional


def buqueda_recursiva_directorio(directorio: str, extension: Optional[str] = None) -> Optional[List[str]]:
    """
    Busca archivos recursivamente en un directorio y sus subdirectorios.

    Args:
        directorio (str): Ruta del directorio donde comenzar la búsqueda
        extension (Optional[str]): Extensión de archivo a filtrar (ej: '.txt'). 
                                Si es None, devuelve todos los archivos.

    Returns:
        Optional[List[str]]: Lista de rutas completas de archivos encontrados, 
                          o None si hay error.

    Raises:
        ValueError: Si el directorio no existe o no es un directorio válido.
    """
    try:
        # Verificar si el directorio existe
        if not os.path.isdir(directorio):
            raise ValueError(f"El directorio '{directorio}' no existe o no es válido")

        archivos_encontrados = []

        for raiz, _, archivos in os.walk(directorio):
            for archivo in archivos:
                ruta_completa = os.path.join(raiz, archivo)
                if extension:
                    if ruta_completa.lower().endswith(extension.lower()):
                        archivos_encontrados.append(ruta_completa)
                else:
                    archivos_encontrados.append(ruta_completa)

        return archivos_encontrados

    except Exception as e:
        print(f"ERROR buscando archivos en {directorio}: {e}")
        return None

    # Ejemplo de uso:
    # Buscar todos los archivos en un directorio:
    # buscar_archivos_recursivos('/ruta/al/directorio')
    #   -> ['/ruta/al/directorio/archivo1.txt', 
    #       '/ruta/al/directorio/subdir/archivo2.pdf', ...]
    #
    # Buscar solo archivos .jpg:
    # buscar_archivos_recursivos('/ruta/al/directorio', '.jpg')
    #   -> ['/ruta/al/directorio/imagen1.jpg',
    #       '/ruta/al/directorio/fotos/imagen2.jpg', ...]
    #
    # Directorio no existe:
    # buscar_archivos_recursivos('/ruta/inexistente')
    #   -> ERROR buscando archivos en /ruta/inexistente: El directorio...
    #   -> None