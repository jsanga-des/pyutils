import pandas as pd
from typing import List, Dict, Optional


def crear_dataframe_desde_datos(datos: List[Dict[str, str]]) -> Optional[pd.DataFrame]:
    """
    Crea un DataFrame de pandas desde una lista de diccionarios.

    Args:
        datos (List[Dict[str, str]]): Lista de datos

    Returns:
        Optional[pd.DataFrame]: DataFrame creado o None si hay error
    """
    try:
        return pd.DataFrame(datos)
    except Exception as e:
        print(f"ERROR creando DataFrame: {e}")
        return None
