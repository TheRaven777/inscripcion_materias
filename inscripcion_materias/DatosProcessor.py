from Estudiante import Estudiante
from Inscripcion import Inscripcion
from Materia import Materia

class DatosProcessor:
    """
    Clase para procesar datos y crear instancias de Estudiante, Materia e Inscripcion.

    Métodos:

    crear_estudiante(cedula: str, nombre: str) -> Estudiante:
        Crea y retorna un objeto Estudiante.

    crear_materia(codigo: str, nombre: str) -> Materia:
        Crea y retorna un objeto Materia.

    crear_inscripcion(estudiante: Estudiante, materia: Materia, numero_inscripcion: int) -> Inscripcion:
        Crea y retorna un objeto Inscripcion.

    procesar_lineas_csv(lineas: list[str]) -> dict:
        Procesa las líneas de un archivo CSV y agrupa las inscripciones por estudiante.
    """
    def _crear_estudiante(self, cedula: str, nombre: str) -> Estudiante:
        return Estudiante(cedula, nombre)

    def _crear_materia(self, codigo: str, nombre: str) -> Materia:
        return Materia(codigo, nombre)

    def _crear_inscripcion(self, estudiante: Estudiante, materia: Materia, numero_inscripcion: int) -> Inscripcion:
        # Al crear la inscripción, agregamos la materia al estudiante
        estudiante.agregar_materia(materia)
        return Inscripcion(estudiante, materia, numero_inscripcion)

    def procesar_lineas_csv(self, lineas: list[str]) -> dict:
        inscripciones_dict = {}
        estudiantes_dict = {}
        numero_inscripcion = 1

        for linea in lineas:
            if linea.strip():
                partes = linea.strip().split(",")
                if len(partes) < 4:
                    print(f"Línea con formato incorrecto: {linea}")
                    continue
                cedula, nombre_estudiante, codigo_materia, nombre_materia = partes

                # Reutiliza el estudiante si ya existe
                if cedula in estudiantes_dict:
                    estudiante = estudiantes_dict[cedula]
                else:
                    estudiante = self._crear_estudiante(cedula, nombre_estudiante)
                    estudiantes_dict[cedula] = estudiante

                # Crea la materia (puedes aplicar una lógica similar para evitar duplicados si lo deseas)
                materia = self._crear_materia(codigo_materia, nombre_materia)
                inscripcion = self._crear_inscripcion(estudiante, materia, numero_inscripcion)
                numero_inscripcion += 1

                if cedula in inscripciones_dict:
                    inscripciones_dict[cedula].append(inscripcion)
                else:
                    inscripciones_dict[cedula] = [inscripcion]
        return inscripciones_dict
