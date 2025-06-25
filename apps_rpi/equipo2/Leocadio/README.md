## ----------------------------- Resultados de Investigación ----------------------------- 

# Acceso a Hardware con Raspberry Pi

# 1. GPIO, I2C, SPI, PWM

+ GPIO:
- Biblioteca: RPi.GPIO, gpiozero
- Instalación:
sudo apt install python3-gpiozero
pip install RPi.GPIO
- Acceso: Control de pines de entrada/salida digitales

+ I2C
- Biblioteca: smbus, adafruit-circuitpython
- Instalación:
sudo apt install python3-smbus i2c-tools
pip install adafruit-circuitpython-busdevice
- Uso: Comunicación con sensores o expansores digitales

+ SPI
- Biblioteca: spidev, adafruit-blinka
- Instalación:
pip install spidev adafruit-blinka
- Uso: Pantallas, memorias o sensores SPI

+ PWM
- Biblioteca: RPi.GPIO, pigpio, gpiozero
- Instalación:
sudo apt install pigpio python3-pigpio
- Uso: Control de motores, servos y brillo de LEDs

_______________________________________________
# 2. Motores Stepper

- Biblioteca: gpiozero.StepperMotor
- Requiere pines digitales para secuencias, o drivers (ULN2003 o A4988)

_______________________________________________
# 3. Acceso a imagen de  una Cámara desde Python
- Biblioteca: opencv-python, picamera2
- Instalación:
pip install opencv-python
sudo apt install python3-picamera2
- Uso:
import cv2
cam = cv2.VideoCapture(0)
ret, frame = cam.read()

________________________________________
# 4. Control de LEDs RGB  (WS2812)
- Biblioteca: rpi_ws281x (v5.0.0)
- Instalación:
pip install rpi_ws281x adafruit-circuitpython-neopixel
- Requiere 5V y un pin GPIO digital

________________________________________
# 5. Acceder a Joystick Logitech F710 desde Python
- Biblioteca: pygame
- Instalación: pip install pygame

- Conectar por  USB en modo XInput o DirectInput

- Para usar:
import pygame
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()


## ----------------------------- Explicación del código ----------------------------- 

- GPIO: se configura el pin como salida y se activa con `GPIO.HIGH`.
- PWM: se usa [GPIO.PWM(pin, frecuencia)] para simular un ciclo de trabajo variable y cambiar el brillo del LED.

## ----------------------------- Aprendizaje Obtenido ------------------------------

- Uso de librerías en Python para manipulación de hardware.
- La SD CARD no se quiere conectar en ubuntu.


## ----------------------------- Ajustes en Ubuntu --------------------------------

- Instalarcion: sudo apt install python3-rpi.gpio
- Asegurarse de que la Raspberry esté corriendo Raspberry Pi OS.
