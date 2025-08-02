# tests/test_buscar_archivos_recursivos.py
import os
import tempfile
import shutil
from functions.buqueda_recursiva_directorio import buqueda_recursiva_directorio

"""
Test para buqueda_recursiva_directorio.py
Ejecutar con: python -m pytest tests/test_buscar_archivos_recursivos.py -v -s
"""


def crear_estructura_prueba():
    """Crea una estructura de directorios temporal para pruebas"""
    temp_dir = tempfile.mkdtemp()

    # Crear estructura de prueba
    os.makedirs(os.path.join(temp_dir, 'subdir1'))
    os.makedirs(os.path.join(temp_dir, 'subdir2', 'subsubdir'))

    # Crear archivos de prueba
    with open(os.path.join(temp_dir, 'archivo1.txt'), 'w') as f:
        f.write("test")
    with open(os.path.join(temp_dir, 'subdir1', 'archivo2.jpg'), 'w') as f:
        f.write("test")
    with open(os.path.join(temp_dir, 'subdir2', 'archivo3.txt'), 'w') as f:
        f.write("test")
    with open(os.path.join(temp_dir, 'subdir2', 'subsubdir', 'archivo4.pdf'), 'w') as f:
        f.write("test")

    return temp_dir


def test_busqueda_recursiva_normal():
    """Test búsqueda recursiva sin filtro de extensión"""
    temp_dir = crear_estructura_prueba()
    print(f"\nProbando búsqueda recursiva en: {temp_dir}")

    resultado = buqueda_recursiva_directorio(temp_dir)

    assert resultado is not None
    assert len(resultado) == 4
    assert all(os.path.exists(f) for f in resultado)
    print(f"  ✓ Encontrados {len(resultado)} archivos correctamente")

    shutil.rmtree(temp_dir)  # Limpieza


def test_busqueda_con_extension():
    """Test búsqueda filtrada por extensión"""
    temp_dir = crear_estructura_prueba()
    print(f"\nProbando búsqueda con extensión .txt en: {temp_dir}")

    resultado = buqueda_recursiva_directorio(temp_dir, '.txt')

    assert resultado is not None
    assert len(resultado) == 2
    assert all(f.endswith('.txt') for f in resultado)
    print(f"  ✓ Encontrados {len(resultado)} archivos .txt")

    shutil.rmtree(temp_dir)  # Limpieza


def test_directorio_inexistente():
    """Test con directorio que no existe"""
    ruta_inexistente = "/ruta/inexistente/123"
    print(f"\nProbando directorio inexistente: {ruta_inexistente}")

    resultado = buqueda_recursiva_directorio(ruta_inexistente)

    assert resultado is None
    print("  ✓ Manejo correcto de directorio inexistente")


def test_directorio_vacio():
    """Test con directorio vacío"""
    temp_dir = tempfile.mkdtemp()
    print(f"\nProbando directorio vacío: {temp_dir}")

    resultado = buqueda_recursiva_directorio(temp_dir)

    assert resultado == []
    print("  ✓ Manejo correcto de directorio vacío")

    shutil.rmtree(temp_dir)  # Limpieza


def test_busqueda_sin_resultados():
    """Test cuando no hay archivos con la extensión solicitada"""
    temp_dir = crear_estructura_prueba()
    print(f"\nProbando búsqueda de .csv en: {temp_dir}")

    resultado = buqueda_recursiva_directorio(temp_dir, '.csv')

    assert resultado == []
    print("  ✓ Manejo correcto cuando no hay resultados")

    shutil.rmtree(temp_dir)  # Limpieza


if __name__ == "__main__":
    # Para ejecutar directamente sin pytest
    test_busqueda_recursiva_normal()
    test_busqueda_con_extension()
    test_directorio_inexistente()
    test_directorio_vacio()
    test_busqueda_sin_resultados()
    print("\n✅ Todas las verificaciones fueron exitosas")