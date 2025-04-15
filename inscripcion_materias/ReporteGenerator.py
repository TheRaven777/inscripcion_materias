# Clase para generar y mostrar el reporte de inscripciones
class ReporteGenerator:
    def mostrar_reporte_inscripciones(self, inscripciones: dict):
        """
        Clase para generar y mostrar reportes de inscripciones.

        Métodos:

        mostrar_reporte_inscripciones(inscripciones: dict):
            Imprime en consola un reporte con las inscripciones agrupadas por estudiante.
        """
        for cedula, inscripciones_list in inscripciones.items():
            # Usamos el primer elemento de la lista para obtener datos del estudiante.
            estudiante = inscripciones_list[0].get_estudiante()
            print(f"\nEstudiante: {estudiante.get_nombre()} - Cédula: {cedula}")
            for inscripcion in inscripciones_list:
                materia = inscripcion.get_materia()
                print(f"\tInscripción #{inscripcion.get_numero_inscripcion()}: {materia.get_nombre()} (Código: {materia.get_codigo()})")
            print(f"\tTotal materias inscritas: {estudiante.total_materias_inscritas()}")
