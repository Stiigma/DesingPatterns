from abc import ABC, abstractmethod
import time
from threading import Thread

# Clase base para los comandos
class Command(ABC):
    @abstractmethod
    def execute(self):
        """Ejecuta el comando."""
        pass

    @abstractmethod
    def undo(self):
        """Deshace el comando."""
        pass

# Comandos concretos
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

class SetBrightnessCommand(Command):
    def __init__(self, light, brightness):
        self.light = light
        self.brightness = brightness
        self.previous_brightness = light.brightness

    def execute(self):
        self.light.set_brightness(self.brightness)

    def undo(self):
        self.light.set_brightness(self.previous_brightness)

class SetColorCommand(Command):
    def __init__(self, light, red, green, blue):
        self.light = light
        self.color = (red, green, blue)
        self.previous_color = light.color

    def execute(self):
        self.light.set_color(*self.color)

    def undo(self):
        self.light.set_color(*self.previous_color)

class ToggleCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.toggle()

    def undo(self):
        self.light.toggle()  # Toggle again to undo

# Clase para manejar la cola de comandos
class CommandQueue:
    def __init__(self, interval=5):
        self.queue = []              # Comandos pendientes
        self.executed_commands = []   # Comandos ejecutados (para deshacer)
        self.interval = interval      # Intervalo en segundos

    def add_command(self, command):
        """Añade un comando a la cola."""
        self.queue.append(command)
        print(f"Comando añadido a la cola: {command.__class__.__name__}")

    def process_queue(self):
        """Procesa todos los comandos en la cola."""
        while self.queue:
            command = self.queue.pop(0)  # Obtiene el primer comando
            print(f"Ejecutando comando: {command.__class__.__name__}")
            command.execute()
            self.executed_commands.append(command)
            time.sleep(self.interval)  # Espera el intervalo definido
        print("Todos los comandos han sido procesados.")

    def undo_last(self):
        """Deshace el último comando ejecutado."""
        if self.executed_commands:
            last_command = self.executed_commands.pop()
            print(f"Deshaciendo comando: {last_command.__class__.__name__}")
            last_command.undo()
        else:
            print("No hay comandos para deshacer.")