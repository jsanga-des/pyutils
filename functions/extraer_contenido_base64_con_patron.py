import re
from typing import Optional


def extraer_contenido_base64_con_patron(contenido: str, patron_regex: str) -> Optional[str]:
    """
    Extrae contenido base64 usando un patrón regex específico.

    Args:
        contenido (str): Contenido del archivo
        patron_regex (str): Patrón regex para extraer el base64

    Returns:
        Optional[str]: Contenido base64 extraído o None si no se encuentra
    """
    match = re.search(patron_regex, contenido, re.DOTALL)
    if not match:
        return None
    return match.group(1).strip()
