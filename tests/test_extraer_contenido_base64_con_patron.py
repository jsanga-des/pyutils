# tests/test_extraer_contenido_base64_con_patron.py

from functions.extraer_contenido_base64_con_patron import extraer_contenido_base64_con_patron

"""
Test para extraer_contenido_base64_con_patron.py
Ejecutar con: python -m pytest tests/test_extraer_contenido_base64_con_patron.py -v -s
"""


def test_extrae_base64_correctamente():
    """Verifica extracción correcta de contenido base64"""
    contenido = """
    Aquí hay un texto previo
    <contenidoBase64>
        aGVsbG8gd29ybGQhCg==
    </contenidoBase64>
    Texto posterior
    """
    patron = r"<contenidoBase64>(.*?)</contenidoBase64>"

    print("\nTEST 1: Extracción de base64 con patrón válido")
    resultado = extraer_contenido_base64_con_patron(contenido, patron)

    print(f"  Contenido esperado: 'aGVsbG8gd29ybGQhCg=='")
    print(f"  Contenido obtenido: '{resultado}'")

    assert resultado == "aGVsbG8gd29ybGQhCg=="
    print("  ✓ Correcto: extrajo el contenido base64 esperado")


def test_no_encuentra_patron():
    """Verifica que devuelve None cuando no hay coincidencia"""
    contenido = "Texto sin patrones base64"
    patron = r"<contenidoBase64>(.*?)</contenidoBase64>"

    print("\nTEST 2: Búsqueda sin patrón existente")
    resultado = extraer_contenido_base64_con_patron(contenido, patron)

    print(f"  Resultado esperado: None")
    print(f"  Resultado obtenido: {resultado}")

    assert resultado is None
    print("  ✓ Correcto: manejo adecuado cuando no hay coincidencia")


def test_patron_complejo():
    """Verifica que funciona con patrones regex complejos"""
    contenido = "|||BEGIN_DATA|||SGVsbG8gV29ybGQ=|||END_DATA|||"
    patron = r"\|\|\|BEGIN_DATA\|\|\|(.*?)\|\|\|END_DATA\|\|\|"

    print("\nTEST 3: Patrón complejo con delimitadores especiales")
    resultado = extraer_contenido_base64_con_patron(contenido, patron)

    print(f"  Contenido esperado: 'SGVsbG8gV29ybGQ='")
    print(f"  Contenido obtenido: '{resultado}'")

    assert resultado == "SGVsbG8gV29ybGQ="
    print("  ✓ Correcto: manejo de patrones complejos")


def test_multiline_content():
    """Verifica que funciona con contenido multi-línea"""
    contenido = """
    StartMarker:
        ABCDEF
        GHIJK
        LMNOP
    EndMarker
    """
    patron = r"StartMarker:(.*?)EndMarker"

    print("\nTEST 4: Contenido multi-línea con espacios")
    resultado = extraer_contenido_base64_con_patron(contenido, patron)
    contenido_esperado = "\n        ABCDEF\n        GHIJK\n        LMNOP\n    "

    print(f"  Contenido esperado: {repr(contenido_esperado)}")
    print(f"  Contenido obtenido: {repr(resultado)}")

    assert resultado.strip() == "ABCDEF\n        GHIJK\n        LMNOP"

    print("  ✓ Correcto: manejo de contenido multi-línea")


def test_verificaciones_completadas():
    """Mensaje final de confirmación"""
    print("\n✅ Todas las verificaciones de extracción base64 fueron exitosas")


if __name__ == "__main__":
    # Para ejecución directa sin pytest
    test_extrae_base64_correctamente()
    test_no_encuentra_patron()
    test_patron_complejo()
    test_multiline_content()
    test_verificaciones_completadas()