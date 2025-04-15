import Materia

class Estudiante:
    """
    Clase para representar un estudiante.

    Métodos:

    total_materias_inscritas() -> int: Retorna la cantidad de materias en las que está inscrito.

    agregar_materia(materia: Materia): Agrega una materia a la lista de inscripciones del estudiante.

    get_cedula() -> str: Retorna la cédula del estudiante.

    get_nombre() -> str: Retorna el nombre del estudiante.
    """
    def __init__(self, cedula: str, nombre: str):
        self._cedula = cedula
        self._nombre = nombre
        # Lista para almacenar las materias en las que el estudiante se inscribió.
        self._materias_inscritas = []

    def total_materias_inscritas(self) -> int:
        return len(self._materias_inscritas)

    def agregar_materia(self, materia: Materia):
        self._materias_inscritas.append(materia)

    def get_cedula(self) -> str:
        return self._cedula

    def get_nombre(self) -> str:
        return self._nombre
