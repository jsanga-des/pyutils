# pyutils

Pequeño conjunto de utilidades Python reutilizables.

## Funciones disponibles

### Manejo de archivos y directorios
- `verificar_carpeta_existe(ruta: str) -> bool`: Verifica si existe una carpeta
- `obtener_archivos_por_extension(ruta_carpeta: str, extension: str) -> List[str]`: Lista archivos con una extensión específica
- `leer_archivo_texto(ruta_archivo: str, encoding: str = 'utf-8') -> Optional[str]`: Lee el contenido de un archivo de texto
- `guardar_dataframe_como_csv(df: pd.DataFrame, nombre_archivo: str) -> bool`: Guarda un DataFrame como archivo CSV
- `guardar_dataframe_como_xlsx(df: pd.DataFrame, nombre_archivo: str) -> bool`: Guarda un DataFrame como archivo Excel

### Manipulación de datos
- `crear_dataframe_desde_datos(todos_los_datos: List[Dict[str, str]]) -> Optional[pd.DataFrame]`: Crea un DataFrame desde una lista de diccionarios
- `decodificar_base64_a_texto(contenido_base64: str, encoding: str = 'utf-8') -> Optional[str]`: Decodifica contenido base64 a texto
- `extraer_contenido_base64_con_patron(contenido: str, patron_regex: str) -> Optional[str]`: Extrae contenido base64 usando un patrón regex

### Patrones y expresiones regulares
- `extraer_contenido_base64_con_patron(contenido: str, patron_regex: str) -> Optional[str]`: Extrae contenido base64 usando un patrón regex específico

