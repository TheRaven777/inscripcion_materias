import Estudiante
import Materia

class Inscripcion:
    """
    Clase para representar una inscripción.

    Métodos:

    get_estudiante() -> Estudiante: Retorna el objeto Estudiante asociado.

    get_materia() -> Materia: Retorna el objeto Materia asociado.

    get_numero_inscripcion() -> int: Retorna el número identificador de la inscripción.
    """
    def __init__(self, estudiante: Estudiante, materia: Materia, numero_inscripcion: int):
        self._estudiante = estudiante
        self._materia = materia
        self._numero_inscripcion = numero_inscripcion

    def get_estudiante(self) -> Estudiante:
        return self._estudiante

    def get_materia(self) -> Materia:
        return self._materia

    def get_numero_inscripcion(self) -> int:
        return self._numero_inscripcion
