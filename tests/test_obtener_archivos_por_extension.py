# tests/test_obtener_archivos_por_extension.py
import os
import tempfile
from functions.obtener_archivos_por_extension import obtener_archivos_por_extension

"""
Test para obtener_archivos_por_extension.py
Ejecutar con: python -m pytest tests/test_obtener_archivos_por_extension.py -v -s
"""


def test_archivos_encontrados(tmp_path):
    """Verifica que encuentra archivos con la extensión correcta"""
    # Crear archivos de prueba
    extension = ".txt"
    archivos_esperados = []

    for i in range(3):
        archivo = tmp_path / f"archivo{i}{extension}"
        archivo.touch()
        archivos_esperados.append(str(archivo))

    # Crear archivos con otra extensión que no deberían ser encontrados
    (tmp_path / "otro_archivo.log").touch()
    (tmp_path / "sin_extension").touch()

    print(f"\nTEST 1: Buscar archivos {extension} en {tmp_path}")
    resultados = obtener_archivos_por_extension(str(tmp_path), extension)

    print(f"  Archivos encontrados: {len(resultados)}")
    print(f"  Archivos esperados: {len(archivos_esperados)}")

    assert len(resultados) == len(archivos_esperados)
    assert all(os.path.exists(archivo) for archivo in resultados)
    print("  ✓ Correcto: encontró todos los archivos esperados")


def test_sin_archivos(tmp_path):
    """Verifica que devuelve lista vacía cuando no hay archivos con la extensión"""
    extension = ".pdf"
    print(f"\nTEST 2: Buscar archivos {extension} (no debería encontrar ninguno)")

    resultados = obtener_archivos_por_extension(str(tmp_path), extension)

    print(f"  Archivos encontrados: {len(resultados)}")
    print(f"  Archivos esperados: 0")

    assert len(resultados) == 0
    print("  ✓ Correcto: no encontró archivos cuando no existen")


def test_carpeta_inexistente():
    """Verifica que devuelve lista vacía cuando la carpeta no existe"""
    ruta_inexistente = "ruta/que/no/existe"
    extension = ".xsig"
    print(f"\nTEST 3: Buscar en carpeta INEXISTENTE ({ruta_inexistente})")

    resultados = obtener_archivos_por_extension(ruta_inexistente, extension)

    print(f"  Resultado obtenido: {len(resultados)} archivos")
    print(f"  Resultado esperado: 0 archivos")

    assert len(resultados) == 0
    print("  ✓ Correcto: manejo adecuado de carpeta inexistente")


def test_case_insensitive(tmp_path):
    """Verifica que la comparación de extensiones no distingue mayúsculas/minúsculas"""
    extension = ".XML"
    archivo_prueba = tmp_path / "archivo.xml"
    archivo_prueba.touch()

    print(f"\nTEST 4: Buscar extensión {extension} (case insensitive)")

    resultados = obtener_archivos_por_extension(str(tmp_path), extension)

    print(f"  Archivos encontrados: {len(resultados)}")
    print(f"  Archivos esperados: 1")

    assert len(resultados) == 1
    print("  ✓ Correcto: encontró archivo con extensión en diferente caso")


def test_verificaciones_completadas():
    """Mensaje final de confirmación"""
    print("\n✅ Todas las verificaciones de archivos por extensión fueron exitosas")


if __name__ == "__main__":
    # Para ejecución directa sin pytest
    with tempfile.TemporaryDirectory() as temp_dir:
        test_archivos_encontrados(temp_dir)
        test_sin_archivos(temp_dir)
    test_carpeta_inexistente()
    with tempfile.TemporaryDirectory() as temp_dir:
        test_case_insensitive(temp_dir)
    test_verificaciones_completadas()