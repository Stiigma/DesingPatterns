# Control de Foco Inteligente con TinyTuya y Patrón de Comando

Este proyecto implementa un sistema de control para un foco inteligente utilizando la librería **TinyTuya** y el **Patrón de Comando** para gestionar operaciones de forma modular y escalable.

---

## Características Principales
- **Control mediante TinyTuya**: Comunicación con dispositivos IoT compatibles con el protocolo Tuya.
- **Patrón de Comando**: Encapsula acciones como comandos independientes para facilitar su gestión.
- **Cola de Comandos**: Ejecuta acciones en secuencia con intervalos personalizables.
- **Función Deshacer**: Revierte el último comando ejecutado fácilmente.

---

## Estructura del Proyecto

 - main.py # Interfaz de usuario y lógica principal
 - light.py # Clase Light para interactuar con el foco
 - command.py # Implementación del Patrón de Comando

---

## Requisitos
- **Python 3.8+**
- **Librería TinyTuya**:
```bash
    pip install tinytuya
```
* **Datos del dispositivo** 

    - device_id: ID del dispositivo (obtenido de la app Tuya o TinyTuya).
    - ip_address: Dirección IP local del foco.
    - local_key: Clave de acceso (vía app Tuya o escaneo con TinyTuya).

### CONFIGURACION

1. Modificar los valores en main.py con los datos de tu dispositivo
2. Ejevuta el programa:
```bash
python main.py
```

## JUSTIFICACION

Este proyecto demuestra cómo el Patrón de Comando puede ser utilizado para gestionar de manera eficiente y flexible las operaciones sobre un foco inteligente. Al encapsular cada acción en un objeto de comando, se logra un diseño modular y extensible que facilita la adición de nuevas funcionalidades y la gestión de operaciones complejas como colas de comandos y deshacer acciones. Además, la integración con TinyTuya permite una comunicación efectiva con dispositivos IoT, lo que hace que este proyecto sea una excelente base para futuras expansiones en el control de dispositivos inteligentes.

