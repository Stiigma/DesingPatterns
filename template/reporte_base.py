from abc import ABC, abstractmethod

class Reporte(ABC):
    def generar(self):
        self.cargar_datos()
        self.procesar_datos()
        contenido = self.generar_contenido()
        self.exportar(contenido)

    def cargar_datos(self):
        print("Cargando datos desde una fuente predeterminada...")

    @abstractmethod
    def procesar_datos(self):
        pass

    @abstractmethod
    def generar_contenido(self):
        pass

    def exportar(self, contenido):
        print("Exportando reporte...")
        with open("reporte.txt", "w", encoding="utf-8") as f:
            f.write(contenido)
        print("Reporte exportado como 'reporte.txt'.")
