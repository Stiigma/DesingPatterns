from reporte_base import Reporte

class ReporteAsistencia(Reporte):
    def __init__(self):
        self.datos = []

    def cargar_datos(self):
        print("Cargando datos de asistencia...")
        self.datos = [
            {"nombre": "Ana", "asistencias": 18, "total": 20},
            {"nombre": "Luis", "asistencias": 15, "total": 20},
            {"nombre": "Carlos", "asistencias": 20, "total": 20}
        ]

    def procesar_datos(self):
        print("Procesando datos de asistencia...")
        for persona in self.datos:
            persona["porcentaje"] = (persona["asistencias"] / persona["total"]) * 100

    def generar_contenido(self):
        print("Generando contenido del reporte de asistencia...")
        contenido = "Reporte de Asistencia\n\n"
        for persona in self.datos:
            contenido += f"{persona['nombre']}: {persona['porcentaje']:.2f}% de asistencia\n"
        return contenido
