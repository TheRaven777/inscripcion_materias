from ArchivoReader import ArchivoReader
from DatosProcessor import DatosProcessor
from ReporteGenerator import ReporteGenerator

class InscripcionesFacade:
    """
    Clase Facade que integra los componentes para gestionar el proceso de inscripciones.

    Métodos:

    obtener_resumen_inscripciones(ruta_archivo: str):
        Coordina la lectura del archivo, el procesamiento de sus datos y la generación del reporte.
    """
    def __init__(self):
        self._archivo_reader = ArchivoReader()
        self._datos_processor = DatosProcessor()
        self._reporte_generator = ReporteGenerator()

    def obtener_resumen_inscripciones(self, ruta_archivo: str):
        """
        Coordina la lectura del archivo CSV, procesa la información y genera el reporte.
        """
        lineas = self._archivo_reader.leer_archivo_csv(ruta_archivo)
        if not lineas:
            print("No se pudo procesar el archivo o está vacío.")
            return

        inscripciones = self._datos_processor.procesar_lineas_csv(lineas)
        self._reporte_generator.mostrar_reporte_inscripciones(inscripciones)


if __name__ == "__main__":
    print("¡Bienvenido al sistema de inscripciones!")
    facade = InscripcionesFacade()
    # Colocar aqui la ruta del archivo CSV de preferencia:
    facade.obtener_resumen_inscripciones(r"C:\Users\loren\OneDrive\Escritorio\ejem.csv")
