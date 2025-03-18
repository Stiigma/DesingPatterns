import tinytuya

class Light:

    def __init__(self, device_id, ip_address, local_key):
        #inicializamos el foco inteligente con lor argumentos de tinytuya

        self.devide = tinytuya.BulbDevice(device_id,ip_address,local_key)
        self.is_on = False
        self.brightness = 100
        self.color = (225,255,255)

    def on(self):
        #self.devide.turn_on()
        self.is_on = True
        print("Ligh is ON")

    def off(self):
        #self.devide.turn_off()
        self.is_on = False
        print("Ligh is OFF")

    def set_brightness(self, brightness):
        #Ajusta el brillo del foco
        if 0 <= brightness <= 100:
            self.device.set_brightness(brightness)
            self.brightness = brightness
            print(f"Brightness set to {brightness}%")
        else:
            print("Brightness must be between 0 and 100")

    def set_color(self, red, green, blue):
        """
        Cambia el color del foco.
        """
        if all(0 <= value <= 255 for value in (red, green, blue)):
            self.device.set_colour(red, green, blue)
            self.color = (red, green, blue)
            print(f"Color set to (R: {red}, G: {green}, B: {blue})")
        else:
            print("Color values must be between 0 and 255")
    
    def toggle(self):
        """Alterna entre encendido y apagado."""
        if self.is_on:
            self.off()
        else:
            self.on()

    def get_status(self):
        """Obtiene y muestra el estado actual del foco."""
        status = self.device.status()
        print("Device Status:", status)
        return status