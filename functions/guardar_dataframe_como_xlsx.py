import pandas as pd


def guardar_dataframe_como_xlsx(df: pd.DataFrame, nombre_archivo: str) -> bool:
    """
    Guarda un DataFrame como archivo Excel.

    Args:
        df (pd.DataFrame): DataFrame a guardar
        nombre_archivo (str): Nombre del archivo

    Returns:
        bool: True si se guardó correctamente, False si hay error
    """
    try:
        df.to_excel(nombre_archivo, index=False, engine='openpyxl')
        print(f"✓ Archivo Excel creado exitosamente: {nombre_archivo}")
        return True
    except ImportError:
        print("ERROR: openpyxl no está instalado. Instala con: pip install openpyxl")
        return False
    except Exception as e:
        print(f"ERROR guardando Excel: {e}")
        return False
