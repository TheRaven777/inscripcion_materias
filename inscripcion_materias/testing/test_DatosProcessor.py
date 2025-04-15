from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from DatosProcessor import DatosProcessor


class TestDatosProcessor(TestCase):
    def test_procesar_linea_valida_csv(self):
        """
        Prueba que al procesar una línea CSV válida se cree un único estudiante con su inscripción.
        """
        # Instancia de DatosProcessor
        procesador = DatosProcessor()

        # Línea CSV de prueba: cédula, nombre_estudiante, codigo_materia, nombre_materia
        linea_entrada_valida = ["1234567,Pepito Perez,1040,Calculo"]
        resultado = procesador.procesar_lineas_csv(linea_entrada_valida)

        # Verificar que el diccionario tenga una única clave
        self.assertEqual(len(resultado), 1, "El diccionario debería tener una única entrada")

        # Verificar que la clave sea '1234567'
        self.assertIn("1234567", resultado, "La cédula '1234567' debe estar en el diccionario")

        # Obtener la lista de inscripciones asociadas al estudiante
        inscripciones = resultado["1234567"]
        self.assertEqual(len(inscripciones), 1, "Debe haber una única inscripción para el estudiante")

        # Validar la inscripción
        inscripcion = inscripciones[0]
        estudiante = inscripcion.get_estudiante()
        materia = inscripcion.get_materia()

        self.assertEqual(estudiante.get_cedula(), "1234567", "La cédula del estudiante no es correcta")
        self.assertEqual(estudiante.get_nombre(), "Pepito Perez", "El nombre del estudiante no es correcto")
        self.assertEqual(materia.get_codigo(), "1040", "El código de la materia no es correcto")
        self.assertEqual(materia.get_nombre(), "Calculo", "El nombre de la materia no es correcto")

    def test_procesar_linea_formato_invalido(self):
        """
        Prueba que una línea con formato inválido sea detectada
        y no se procese ninguna inscripción.
        """
        procesador = DatosProcessor()
        linea_entrada_invalida = ["1234567,Pepito Perez"]  # Solo 2 campos en lugar de 4

        with patch('sys.stdout', new=StringIO()) as fake_out:
            resultado = procesador.procesar_lineas_csv(linea_entrada_invalida)
            salida = fake_out.getvalue().strip()

        # Validar que el mensaje de error se haya impreso
        self.assertIn("Línea con formato incorrecto: 1234567,Pepito Perez", salida)

        # Validar que el resultado sea un diccionario vacío
        self.assertEqual(resultado, {}, "El resultado debe ser un diccionario vacío al fallar la línea")

    def test_procesar_lineas_csv_multiples_materias_mismo_estudiante(self):
        """
        Prueba que un mismo estudiante pueda estar inscrito en múltiples materias
        y que se cree solo un objeto Estudiante con múltiples inscripciones.
        """
        procesador = DatosProcessor()
        lineas = ["1234567,Pepito Perez,1040,Calculo", "1234567,Pepito Perez,1060,Administracion"]

        resultado = procesador.procesar_lineas_csv(lineas)

        # Validar que solo haya un estudiante en el diccionario
        self.assertEqual(len(resultado), 1, "Debe haber un solo estudiante en el diccionario")
        self.assertIn("1234567", resultado, "La cédula '1234567' debe estar presente en el resultado")

        inscripciones = resultado["1234567"]

        # Validar que haya dos inscripciones
        self.assertEqual(len(inscripciones), 2, "Deben existir dos inscripciones para el estudiante")

        materias_codigos = {insc.get_materia().get_codigo() for insc in inscripciones}

        # Validar que las materias sean las esperadas
        self.assertSetEqual(materias_codigos, {"1040", "1060"},"Las materias inscritas no corresponden con las esperadas")
