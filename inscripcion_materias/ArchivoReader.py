class ArchivoReader:
    """
    Clase para leer archivos CSV.

    Métodos:

    leer_archivo_csv(ruta_archivo: str) -> list[str]:
        Lee un archivo CSV y retorna una lista de líneas.
    """
    def leer_archivo_csv(self, ruta_archivo: str) -> list[str]:
        """
        Lee el archivo CSV línea por línea y devuelve una lista de cadenas.
        """
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
            print(f"Archivo '{ruta_archivo}' leído exitosamente.")
            return lineas
        except FileNotFoundError:
            print(f"Error: El archivo '{ruta_archivo}' no se encontró.")
            return []
