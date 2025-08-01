import pandas as pd


def guardar_dataframe_como_csv(df: pd.DataFrame, nombre_archivo: str) -> bool:
    """
    Guarda un DataFrame como archivo CSV.

    Args:
        df (pd.DataFrame): DataFrame a guardar
        nombre_archivo (str): Nombre del archivo

    Returns:
        bool: True si se guardó correctamente, False si hay error
    """
    try:
        df.to_csv(nombre_archivo, index=False, encoding='utf-8-sig')
        print(f"✓ Archivo CSV creado exitosamente: {nombre_archivo}")
        return True
    except Exception as e:
        print(f"ERROR guardando CSV: {e}")
        return False
