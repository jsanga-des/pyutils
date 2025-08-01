# tests/test_guardar_dataframe_como_csv.py
import pandas as pd
import os
import tempfile
from unittest.mock import patch
from functions.guardar_dataframe_como_csv import guardar_dataframe_como_csv

"""
Test para guardar_dataframe_como_csv.py
Ejecutar con: python -m pytest tests/test_guardar_dataframe_como_csv.py -v -s
"""


def test_guardado_exitoso():
    """Verifica guardado exitoso de DataFrame a CSV"""
    df = pd.DataFrame({
        'Nombre': ['Alice', 'Bob', 'Charlie'],
        'Edad': [25, 30, 35],
        'Ciudad': ['NY', 'LA', 'Chicago']
    })

    with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as tmp:
        nombre_archivo = tmp.name

    print("\nTEST 1: Guardado exitoso de DataFrame")
    resultado = guardar_dataframe_como_csv(df, nombre_archivo)

    assert resultado is True
    assert os.path.exists(nombre_archivo)
    assert os.path.getsize(nombre_archivo) > 0

    # Verificar contenido básico
    with open(nombre_archivo, 'r', encoding='utf-8-sig') as f:
        contenido = f.read()
        assert 'Nombre,Edad,Ciudad' in contenido
        assert 'Alice,25,NY' in contenido

    print(f"  ✓ Archivo creado correctamente: {nombre_archivo}")

    # Limpieza
    os.unlink(nombre_archivo)


def test_guardado_error_permisos():
    """Verifica manejo de error de permisos"""
    df = pd.DataFrame({'A': [1, 2, 3]})
    ruta_protegida = "/directorio_protegido/test.csv" if os.name == 'posix' else "C:\\Windows\\System32\\test.csv"

    print("\nTEST 2: Simulación de error de permisos")
    resultado = guardar_dataframe_como_csv(df, ruta_protegida)

    assert resultado is False
    print("  ✓ Correcto: Manejo de error de permisos")


def test_dataframe_vacio():
    """Verifica guardado de DataFrame vacío"""
    df = pd.DataFrame()

    with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as tmp:
        nombre_archivo = tmp.name

    print("\nTEST 3: Guardado de DataFrame vacío")
    resultado = guardar_dataframe_como_csv(df, nombre_archivo)

    assert resultado is True
    assert os.path.exists(nombre_archivo)

    # Verificar que solo contiene encabezados vacíos
    with open(nombre_archivo, 'r', encoding='utf-8-sig') as f:
        contenido = f.read()
        assert contenido == '\n'  # Solo nueva línea para DataFrame vacío

    print("  ✓ Correcto: Guardado de DataFrame vacío")

    # Limpieza
    os.unlink(nombre_archivo)


def test_nombre_archivo_invalido():
    """Verifica manejo de nombre de archivo inválido"""
    df = pd.DataFrame({'A': [1, 2, 3]})

    print("\nTEST 4: Nombre de archivo inválido")
    resultado = guardar_dataframe_como_csv(df, "/ruta/invalida/\0caracteres.csv")

    assert resultado is False
    print("  ✓ Correcto: Manejo de nombre de archivo inválido")


def test_caracteres_especiales():
    """Verifica guardado con caracteres especiales"""
    df = pd.DataFrame({
        'Texto': ['Español', 'Français', '日本語'],
        'Símbolos': ['€', '®', '∞']
    })

    with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as tmp:
        nombre_archivo = tmp.name

    print("\nTEST 5: Caracteres especiales y Unicode")
    resultado = guardar_dataframe_como_csv(df, nombre_archivo)

    assert resultado is True

    # Verificar que los caracteres especiales se guardaron correctamente
    with open(nombre_archivo, 'r', encoding='utf-8-sig') as f:
        contenido = f.read()
        assert 'Español' in contenido
        assert '日本語' in contenido
        assert '€' in contenido

    print("  ✓ Correcto: Guardado de caracteres especiales")

    # Limpieza
    os.unlink(nombre_archivo)


def test_verificaciones_completadas():
    """Mensaje final de confirmación"""
    print("\n✅ Todas las verificaciones de guardado de CSV fueron exitosas")


if __name__ == "__main__":
    # Para ejecución directa sin pytest
    test_guardado_exitoso()
    test_guardado_error_permisos()
    test_dataframe_vacio()
    test_nombre_archivo_invalido()
    test_caracteres_especiales()
    test_verificaciones_completadas()