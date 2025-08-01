# functions/verificar_carpeta_existe.py
import os


def verificar_carpeta_existe(ruta_carpeta: str) -> bool:
    """
    Verifica si una carpeta existe.

    Args:
        ruta_carpeta (str): Ruta de la carpeta a verificar

    Returns:
        bool: True si existe, False si no
    """
    return os.path.exists(ruta_carpeta) and os.path.isdir(ruta_carpeta)
