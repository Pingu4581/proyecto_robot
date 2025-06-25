# test_rgb_leds.py
"""
Nombre: Tu Nombre
Equipo: 2
Dispositivo: LED rojo (o componente del RGB)
Rol: Salida
Descripción: Encender y apagar un LED usando GPIO
"""

import RPi.GPIO as GPIO
import time

# 🔧 Setup: definir e inicializar pines y objetos
def setup():
    GPIO.setmode(GPIO.BCM)  # Usar numeración BCM
    GPIO.setwarnings(False)
    led_pin = 17  # GPIO17 = pin físico 11
    GPIO.setup(led_pin, GPIO.OUT)
    print("[INFO] LED listo en GPIO17")
    return led_pin

# 🔁 Loop principal: encender/apagar
def loop(pin):
    print("[INFO] Ejecutando prueba. Presiona Ctrl+C para salir.")
    try:
        while True:
            GPIO.output(pin, GPIO.HIGH)  # Encender
            print("LED ON")
            time.sleep(1)
            GPIO.output(pin, GPIO.LOW)   # Apagar
            print("LED OFF")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] Prueba interrumpida por el usuario.")
        GPIO.cleanup()

if __name__ == "__main__":
    led_pin = setup()
    loop(led_pin)

