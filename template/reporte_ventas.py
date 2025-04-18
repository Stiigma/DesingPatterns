from reporte_base import Reporte

class ReporteVentas(Reporte):
    def __init__(self):
        self.datos = []

    def cargar_datos(self):
        print("Cargando datos de ventas...")
        self.datos = [
            {"producto": "Laptop", "cantidad": 4, "precio": 1200},
            {"producto": "Mouse", "cantidad": 10, "precio": 25},
            {"producto": "Teclado", "cantidad": 5, "precio": 45}
        ]

    def procesar_datos(self):
        print("Procesando datos de ventas...")
        for item in self.datos:
            item["total"] = item["cantidad"] * item["precio"]

    def generar_contenido(self):
        print("Generando contenido del reporte de ventas...")
        contenido = "Reporte de Ventas\n\n"
        total_general = 0
        for item in self.datos:
            contenido += f"{item['producto']}: {item['cantidad']} unidades x ${item['precio']} = ${item['total']}\n"
            total_general += item["total"]
        contenido += f"\nTotal General: ${total_general}\n"
        return contenido
