import os
import tempfile
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from ArchivoReader import ArchivoReader

class TestArchivoReader(TestCase):
    def setUp(self):
        # Instancia de ArchivoReader a utilizar en las pruebas.
        self.archivo_reader = ArchivoReader()

    def test_leer_archivo_csv_con_contenido(self):
        """
        Prueba de leer un archivo CSV válido con contenido.
        Se verifica que se retorne una lista con las líneas correctas
        y que se imprima el mensaje de éxito.
        """
        # Contenido de ejemplo con dos líneas. La primera línea termina en salto de línea.
        contenido = "1234567,Pepito Perez,1040,Calculo\n9876534,Juan Gómez,1050,Física"
        # Crear un archivo temporal con este contenido.
        with tempfile.NamedTemporaryFile(mode="w+", delete=False, encoding="utf-8") as temp:
            temp.write(contenido)
            temp_path = temp.name

        try:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                lineas = self.archivo_reader.leer_archivo_csv(temp_path)
                salida = fake_out.getvalue().strip()

            # Se usa splitlines(keepends=True) para conservar los saltos de línea
            lineas_esperadas = contenido.splitlines(keepends=True)
            self.assertEqual(lineas, lineas_esperadas, "El contenido leído no coincide con el esperado.")
            self.assertIn("leído exitosamente", salida, "El mensaje de éxito no aparece en la salida.")
        finally:
            os.remove(temp_path)

    def test_leer_archivo_csv_vacio(self):
        """
        Prueba de leer un archivo CSV vacío.
        Se verifica que se retorne una lista vacía y se imprima el mensaje de éxito.
        """
        # Crear un archivo temporal vacío.
        with tempfile.NamedTemporaryFile(mode="w+", delete=False, encoding="utf-8") as temp:
            temp_path = temp.name

        try:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                lineas = self.archivo_reader.leer_archivo_csv(temp_path)
                salida = fake_out.getvalue().strip()

            self.assertEqual(lineas, [], "Al leer un archivo vacío, debe retornar una lista vacía.")
            self.assertIn("leído exitosamente", salida,
                          "El mensaje de éxito debe indicarse incluso para archivos vacíos.")
        finally:
            os.remove(temp_path)

    def test_leer_archivo_csv_no_existente(self):
        """
        Prueba de intentar leer un archivo CSV que no existe.
        Se verifica que se retorne una lista vacía y se imprima el mensaje de error adecuado.
        """
        ruta_inexistente = "ruta/no/existe.csv"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            lineas = self.archivo_reader.leer_archivo_csv(ruta_inexistente)
            salida = fake_out.getvalue().strip()

        self.assertEqual(lineas, [], "Al no encontrar el archivo, debe retornar una lista vacía.")
        self.assertIn("Error: El archivo", salida,
                      "El mensaje de error no se mostró correctamente para un archivo inexistente.")