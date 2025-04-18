import os
from reporte_ventas import ReporteVentas
from reporte_asistencia import ReporteAsistencia

class TestReporteVentas:

    def test_generacion_reporte_ventas(self, capsys):
        reporte = ReporteVentas()
        reporte.generar()
        salida = capsys.readouterr().out

        # Verifica los prints esperados
        assert "Cargando datos de ventas..." in salida
        assert "Procesando datos de ventas..." in salida
        assert "Generando contenido del reporte de ventas..." in salida
        assert "Exportando reporte..." in salida

        # Verifica el contenido del archivo generado
        with open("reporte.txt", "r", encoding="utf-8") as f:
            contenido = f.read()

        assert "Laptop: 4 unidades" in contenido or "Mouse: 10 unidades" in contenido
        assert "Total General" in contenido

        # Limpieza del archivo generado
        #os.remove("reporte.txt")


class TestReporteAsistencia:

    def test_generacion_reporte_asistencia(self, capsys):
        reporte = ReporteAsistencia()
        reporte.generar()
        salida = capsys.readouterr().out

        # Verifica los prints esperados
        assert "Cargando datos de asistencia..." in salida
        assert "Procesando datos de asistencia..." in salida
        assert "Generando contenido del reporte de asistencia..." in salida
        assert "Exportando reporte..." in salida

        # Verifica el contenido del archivo generado
        with open("reporte.txt", "r", encoding="utf-8") as f:
            contenido = f.read()

        assert "Ana: " in contenido or "Carlos: " in contenido
        assert "%" in contenido

        # Limpieza del archivo generado
        #os.remove("reporte.txt")
