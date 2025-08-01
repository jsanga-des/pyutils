# tests/test_guardar_dataframe_como_xlsx.py
import pandas as pd
import os
import tempfile
from unittest.mock import patch
from functions.guardar_dataframe_como_xlsx import guardar_dataframe_como_xlsx

"""
Test para guardar_dataframe_como_xlsx.py
Ejecutar con: python -m pytest tests/test_guardar_dataframe_como_xlsx.py -v -s
"""


def test_guardado_exitoso():
    """Verifica guardado exitoso de DataFrame a Excel"""
    df = pd.DataFrame({
        'Nombre': ['Alice', 'Bob', 'Charlie'],
        'Edad': [25, 30, 35],
        'Ciudad': ['NY', 'LA', 'Chicago']
    })

    with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp:
        nombre_archivo = tmp.name

    print("\nTEST 1: Guardado exitoso de DataFrame")
    resultado = guardar_dataframe_como_xlsx(df, nombre_archivo)

    assert resultado is True
    assert os.path.exists(nombre_archivo)
    assert os.path.getsize(nombre_archivo) > 0
    print(f"  ✓ Archivo creado correctamente: {nombre_archivo}")

    # Limpieza
    os.unlink(nombre_archivo)


def test_guardado_sin_openpyxl():
    """Verifica manejo cuando openpyxl no está instalado"""
    df = pd.DataFrame({'A': [1, 2, 3]})

    print("\nTEST 2: Simulación de openpyxl no instalado")
    with patch('pandas.DataFrame.to_excel', side_effect=ImportError("openpyxl not found")):
        resultado = guardar_dataframe_como_xlsx(df, "test.xlsx")

    assert resultado is False
    print("  ✓ Correcto: Manejo de falta de openpyxl")


def test_guardado_error_permisos():
    """Verifica manejo de error de permisos"""
    df = pd.DataFrame({'A': [1, 2, 3]})
    ruta_protegida = "/directorio_protegido/test.xlsx" if os.name == 'posix' else "C:\\Windows\\System32\\test.xlsx"

    print("\nTEST 3: Simulación de error de permisos")
    resultado = guardar_dataframe_como_xlsx(df, ruta_protegida)

    assert resultado is False
    print("  ✓ Correcto: Manejo de error de permisos")


def test_dataframe_vacio():
    """Verifica guardado de DataFrame vacío"""
    df = pd.DataFrame()

    with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp:
        nombre_archivo = tmp.name

    print("\nTEST 4: Guardado de DataFrame vacío")
    resultado = guardar_dataframe_como_xlsx(df, nombre_archivo)

    assert resultado is True
    assert os.path.exists(nombre_archivo)
    print("  ✓ Correcto: Guardado de DataFrame vacío")

    # Limpieza
    os.unlink(nombre_archivo)


def test_nombre_archivo_invalido():
    """Verifica manejo de nombre de archivo inválido"""
    df = pd.DataFrame({'A': [1, 2, 3]})

    print("\nTEST 5: Nombre de archivo inválido")
    resultado = guardar_dataframe_como_xlsx(df, "/ruta/invalida/\0caracteres.xlsx")

    assert resultado is False
    print("  ✓ Correcto: Manejo de nombre de archivo inválido")


def test_verificaciones_completadas():
    """Mensaje final de confirmación"""
    print("\n✅ Todas las verificaciones de guardado de Excel fueron exitosas")


if __name__ == "__main__":
    # Para ejecución directa sin pytest
    test_guardado_exitoso()
    test_guardado_sin_openpyxl()
    test_guardado_error_permisos()
    test_dataframe_vacio()
    test_nombre_archivo_invalido()
    test_verificaciones_completadas()