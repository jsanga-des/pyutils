import os
from typing import Optional


def leer_archivo_texto(ruta_archivo: str, encoding: str = 'utf-8') -> Optional[str]:
    """
    Lee el contenido completo de un archivo de texto.

    Args:
        ruta_archivo (str): Ruta del archivo
        encoding (str): Codificación del archivo

    Returns:
        Optional[str]: Contenido del archivo o None si hay error
    """
    try:
        with open(ruta_archivo, 'r', encoding=encoding) as f:
            return f.read()
    except Exception as e:
        print(f"  ERROR leyendo archivo {os.path.basename(ruta_archivo)}: {e}")
        return None
