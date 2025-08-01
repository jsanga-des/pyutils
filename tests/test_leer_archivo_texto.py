# tests/test_leer_archivo_texto.py
import os
import tempfile
from functions.leer_archivo_texto import leer_archivo_texto

"""
Lee el contenido completo de un archivo de texto.
python -m pytest tests/test_leer_archivo_texto.py -v -s
"""

def test_leer_archivo_existente():
    """Test lectura exitosa de archivo"""
    # Crear archivo temporal con contenido
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as f:
        f.write("Contenido de prueba\nSegunda línea")
        ruta_archivo = f.name

    print(f"\nProbando archivo existente: {ruta_archivo}")
    resultado = leer_archivo_texto(ruta_archivo)

    assert resultado == "Contenido de prueba\nSegunda línea"
    print(f"  ✓ Archivo leído correctamente")

    os.unlink(ruta_archivo)  # Limpieza


def test_leer_archivo_inexistente():
    """Test archivo que no existe"""
    ruta_inexistente = "archivo_que_no_existe.txt"
    print(f"\nProbando archivo inexistente: {ruta_inexistente}")

    resultado = leer_archivo_texto(ruta_inexistente)

    assert resultado is None
    print("  ✓ Manejo correcto de archivo inexistente")


def test_leer_archivo_encoding_incorrecto():
    """Test con encoding incorrecto"""
    contenido = "Texto con caracteres especiales ñáéíóú"

    # Crear archivo con encoding latin-1
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='latin-1') as f:
        f.write(contenido)
        ruta_archivo = f.name

    print(f"\nProbando encoding incorrecto: {ruta_archivo}")
    resultado = leer_archivo_texto(ruta_archivo, encoding='utf-8')

    assert resultado is None
    print("  ✓ Manejo correcto de error de encoding")

    os.unlink(ruta_archivo)


def test_leer_archivo_vacio():
    """Test archivo vacío"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as f:
        ruta_archivo = f.name

    print(f"\nProbando archivo vacío: {ruta_archivo}")
    resultado = leer_archivo_texto(ruta_archivo)

    assert resultado == ""
    print("  ✓ Archivo vacío leído correctamente")

    os.unlink(ruta_archivo)


if __name__ == "__main__":
    # Para ejecutar directamente sin pytest
    test_leer_archivo_existente()
    test_leer_archivo_inexistente()
    test_leer_archivo_encoding_incorrecto()
    test_leer_archivo_vacio()
    print("\n✅ Todos los tests pasaron!")