import base64
from typing import Optional


def decodificar_base64_a_texto(contenido_base64: str, encoding: str = 'utf-8') -> Optional[str]:
    """
    Decodifica contenido base64 a texto.

    Args:
        contenido_base64 (str): Contenido en base64
        encoding (str): Codificación para decodificar

    Returns:
        Optional[str]: Texto decodificado o None si hay error
    """
    try:
        return base64.b64decode(contenido_base64).decode(encoding)
    except Exception as e:
        print(f"  ERROR decodificando base64: {e}")
        return None
