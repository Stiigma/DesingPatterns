from reporte_ventas import ReporteVentas
from reporte_asistencia import ReporteAsistencia

def main():
    print("=== Generando Reporte de Ventas ===")
    reporte_ventas = ReporteVentas()
    reporte_ventas.generar()

    # print("\n=== Generando Reporte de Asistencia ===")
    # reporte_asistencia = ReporteAsistencia()
    # reporte_asistencia.generar()

if __name__ == "__main__":
    main()
