# tests/test_crear_dataframe_desde_datos.py
import pandas as pd
from functions.crear_dataframe_desde_datos import crear_dataframe_desde_datos

"""
Test para crear_dataframe_desde_datos.py
Ejecutar con: python -m pytest tests/test_crear_dataframe_desde_datos.py -v -s
"""


def test_creacion_correcta_dataframe():
    """Verifica creación exitosa de DataFrame"""
    datos = [
        {"nombre": "Alice", "edad": "25", "ciudad": "Nueva York"},
        {"nombre": "Bob", "edad": "30", "ciudad": "Chicago"},
        {"nombre": "Charlie", "edad": "35", "ciudad": "Los Ángeles"}
    ]

    print("\nTEST 1: Creación correcta de DataFrame")
    resultado = crear_dataframe_desde_datos(datos)

    assert isinstance(resultado, pd.DataFrame)
    assert len(resultado) == 3
    assert list(resultado.columns) == ["nombre", "edad", "ciudad"]
    print("  ✓ Correcto: DataFrame creado con estructura esperada")


def test_dataframe_vacio():
    """Verifica manejo de lista vacía"""
    print("\nTEST 2: Creación con lista vacía")
    resultado = crear_dataframe_desde_datos([])

    assert isinstance(resultado, pd.DataFrame)
    assert resultado.empty
    print("  ✓ Correcto: DataFrame vacío creado")


def test_estructura_inconsistente():
    """Verifica manejo de diccionarios con estructura inconsistente"""
    datos = [
        {"nombre": "Alice", "edad": "25"},
        {"nombre": "Bob", "ciudad": "Chicago"},
        {"nombre": "Charlie", "edad": "35", "pais": "USA"}
    ]

    print("\nTEST 3: Estructura inconsistente en datos")
    resultado = crear_dataframe_desde_datos(datos)

    assert isinstance(resultado, pd.DataFrame)
    assert set(resultado.columns) == {"nombre", "edad", "ciudad", "pais"}
    assert resultado["edad"].isna().sum() == 1  # Debe tener un valor NaN
    print("  ✓ Correcto: Manejo adecuado de estructura inconsistente")


def test_tipos_datos_mezclados():
    """Verifica manejo de tipos de datos mezclados"""
    datos = [
        {"id": "1", "valor": "100"},
        {"id": 2, "valor": 200},  # Tipos diferentes
        {"id": "3", "valor": "300"}
    ]

    print("\nTEST 4: Tipos de datos mezclados")
    resultado = crear_dataframe_desde_datos(datos)

    assert isinstance(resultado, pd.DataFrame)
    assert len(resultado) == 3
    print("  ✓ Correcto: Manejo de tipos de datos mezclados")


def test_datos_invalidos():
    """Verifica manejo de datos completamente inválidos"""
    print("\nTEST 5: Datos inválidos (no lista de diccionarios)")
    resultado = crear_dataframe_desde_datos("esto no es una lista")

    assert resultado is None
    print("  ✓ Correcto: Devuelve None para datos inválidos")


def test_verificaciones_completadas():
    """Mensaje final de confirmación"""
    print("\n✅ Todas las verificaciones de creación de DataFrame fueron exitosas")


if __name__ == "__main__":
    # Para ejecución directa sin pytest
    test_creacion_correcta_dataframe()
    test_dataframe_vacio()
    test_estructura_inconsistente()
    test_tipos_datos_mezclados()
    test_datos_invalidos()
    test_verificaciones_completadas()