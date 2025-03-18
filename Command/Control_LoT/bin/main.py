import sys
import os

# Añadir la ruta del proyecto al sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from lib.light import Light
from lib.command import (
    LightOnCommand,
    LightOffCommand,
    SetBrightnessCommand,
    SetColorCommand,
    ToggleCommand,
    CommandQueue,
)


def print_menu():
    print("\n--- Control de Foco Inteligente (Modo Cola) ---")
    print("1. Agregar 'Encender' a la cola")
    print("2. Agregar 'Apagar' a la cola")
    print("3. Agregar 'Ajustar Brillo' a la cola")
    print("4. Agregar 'Cambiar Color' a la cola")
    print("5. Agregar 'Alternar' a la cola")
    print("6. Procesar todos los comandos en la cola")
    print("7. Deshacer el último comando ejecutado")
    print("8. Salir")

def main():
    # Configuración del foco (reemplaza con tus datos)
    device_id = "eb2a61de2334a298c5vabf"
    ip_address = "192.168.1.100"
    local_key = "abc123def456"

    light = Light(device_id, ip_address, local_key)
    command_queue = CommandQueue(interval=1)  # Intervalo de 5 segundos

    while True:
        print_menu()
        choice = input("Elige una opción: ")

        if choice == "1":
            command_queue.add_command(LightOnCommand(light))
        elif choice == "2":
            command_queue.add_command(LightOffCommand(light))
        elif choice == "3":
            brightness = int(input("Ingresa el brillo (0-100): "))
            command_queue.add_command(SetBrightnessCommand(light, brightness))
        elif choice == "4":
            red = int(input("Ingresa el valor de Rojo (0-255): "))
            green = int(input("Ingresa el valor de Verde (0-255): "))
            blue = int(input("Ingresa el valor de Azul (0-255): "))
            command_queue.add_command(SetColorCommand(light, red, green, blue))
        elif choice == "5":
            command_queue.add_command(ToggleCommand(light))
        elif choice == "6":
            print("Procesando la cola de comandos...")
            command_queue.process_queue()
        elif choice == "7":
            command_queue.undo_last()
        elif choice == "8":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()