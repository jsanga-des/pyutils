# tests/test_decodificar_base64_a_texto.py
import base64
from functions.decodificar_base64_a_texto import decodificar_base64_a_texto

"""
Test para decodificar_base64_a_texto.py
Ejecutar con: python -m pytest tests/test_decodificar_base64_a_texto.py -v -s
"""


def test_decodificacion_correcta():
    """Verifica decodificación exitosa de base64 a texto"""
    texto_original = "Hola mundo desde Python!"
    contenido_base64 = base64.b64encode(texto_original.encode('utf-8')).decode('utf-8')

    print("\nTEST 1: Decodificación básica correcta")
    resultado = decodificar_base64_a_texto(contenido_base64)

    print(f"  Texto esperado: '{texto_original}'")
    print(f"  Texto obtenido: '{resultado}'")

    assert resultado == texto_original
    print("  ✓ Correcto: decodificación exitosa")


def test_decodificacion_con_encoding():
    """Verifica decodificación con diferentes encodings"""
    texto_original = "Texto con ñ y acentos áéíóú"
    contenido_base64 = base64.b64encode(texto_original.encode('latin-1')).decode('latin-1')

    print("\nTEST 2: Decodificación con encoding latin-1")
    resultado = decodificar_base64_a_texto(contenido_base64, encoding='latin-1')

    print(f"  Texto esperado: '{texto_original}'")
    print(f"  Texto obtenido: '{resultado}'")

    assert resultado == texto_original
    print("  ✓ Correcto: manejo de encoding específico")


def test_base64_invalido():
    """Verifica manejo de base64 mal formado"""
    contenido_invalido = "Esto no es base64 válido!"

    print("\nTEST 3: Intento de decodificar base64 inválido")
    resultado = decodificar_base64_a_texto(contenido_invalido)

    print(f"  Resultado esperado: None")
    print(f"  Resultado obtenido: {resultado}")

    assert resultado is None
    print("  ✓ Correcto: manejo de base64 inválido")


def test_caracteres_no_ascii():
    """Verifica decodificación con caracteres especiales"""
    texto_original = "こんにちは世界"  # Hola mundo en japonés
    contenido_base64 = base64.b64encode(texto_original.encode('utf-8')).decode('utf-8')

    print("\nTEST 4: Caracteres no ASCII")
    resultado = decodificar_base64_a_texto(contenido_base64)

    print(f"  Texto esperado: '{texto_original}'")
    print(f"  Texto obtenido: '{resultado}'")

    assert resultado == texto_original
    print("  ✓ Correcto: manejo de caracteres no ASCII")


def test_string_vacio():
    """Verifica manejo de string vacío"""
    print("\nTEST 5: Cadena base64 vacía")
    resultado = decodificar_base64_a_texto("")

    print(f"  Resultado esperado: '' (cadena vacía)")
    print(f"  Resultado obtenido: '{resultado}'")

    assert resultado == ""  # Cambiar la assertion
    print("  ✓ Correcto: devuelve cadena vacía para input vacío")


def test_verificaciones_completadas():
    """Mensaje final de confirmación"""
    print("\n✅ Todas las verificaciones de decodificación fueron exitosas")


if __name__ == "__main__":
    # Para ejecución directa sin pytest
    test_decodificacion_correcta()
    test_decodificacion_con_encoding()
    test_base64_invalido()
    test_caracteres_no_ascii()
    test_string_vacio()
    test_verificaciones_completadas()