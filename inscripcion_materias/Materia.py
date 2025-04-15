class Materia:
    """
    Clase para representar una materia.

    Métodos:

    get_codigo() -> str: Retorna el código de la materia.

    get_nombre() -> str: Retorna el nombre de la materia.
    """
    def __init__(self, codigo: str, nombre: str):
        self._codigo = codigo
        self._nombre = nombre

    def get_codigo(self) -> str:
        return self._codigo

    def get_nombre(self) -> str:
        return self._nombre
