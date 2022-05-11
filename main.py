from flask import Flask
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
import serial
import sys
import time

app = Flask(__name__)

BASE_URL = "/api"
LIGHT = "/light"
CUARTO = "/cuarto"
COCINA = "/cocina"
BANIO = "/banio"
DOOR = "/puerta"

LED_CUARTO = 22
LED_COCINA = 23
LED_BANIO = 24
MOTOR = 17

def peripheral_setup():
    GPIO.setmode(GPIO.BCM) #puede cambiar a BOARD
    GPIO.setup(LED_CUARTO, GPIO.OUT)
    GPIO.setup(LED_COCINA, GPIO.OUT)
    GPIO.setup(LED_BANIO, GPIO.OUT)
    GPIO.setup(MOTOR, GPIO.OUT)


def light_cuarto_on():
    GPIO.output(LED_CUARTO,GPIO.HIGH)

def light_cuarto_off():
    GPIO.output(LED_CUARTO,GPIO.LOW)

def light_cocina_on():
    GPIO.output(LED_COCINA,GPIO.HIGH)

def light_cocina_off():
    GPIO.output(LED_COCINA,GPIO.LOW)

def light_banio_on():
    GPIO.output(LED_BANIO,GPIO.HIGH)

def light_banio_off():
    GPIO.output(LED_BANIO,GPIO.LOW)

def door_up_gp():
    p = GPIO.PWM(MOTOR, 50)
    p.start(2.5)
    #p.ChangeDutyCycle(2.5)
    #time.sleep(1)
    #p.ChangeDutyCycle(7.5)
    i = 2.5
    while i <= 7.5:
        p.ChangeDutyCycle(i)
        i+= 0.25
        time.sleep(0.1)
    p.stop()

def door_down_gp():
    p = GPIO.PWM(MOTOR, 50)
    p.start(7.5)
    i = 7.5
    while i >= 2.5:
        p.ChangeDutyCycle(i)
        i -= 0.25
        time.sleep(0.1)
    p.stop()

def light_arduino_on():
    ser = serial.Serial('/dev/serial0', 9600, timeout=1)
    ser.write("1".encode())
    response = ""
    while response == "":
        response = ser.readline().decode()
    print(response)
    ser.close()

def light_arduino_off():
    ser = serial.Serial('/dev/serial0', 9600, timeout=1)
    ser.write("2".encode())
    response = ""
    while response == "":
        response = ser.readline().decode()
    print(response)
    ser.close()


def light_arduino_low():
    ser = serial.Serial('/dev/serial0', 9600, timeout=1)
    ser.write("3".encode())
    response = ""
    while response == "":
        response = ser.readline().decode()
    print(response)
    ser.close()

def light_arduino_medium():
    ser = serial.Serial('/dev/serial0', 9600, timeout=1)
    ser.write("4".encode())
    response = ""
    while response == "":
        response = ser.readline().decode()
    print(response)
    ser.close()

def light_arduino_high():
    ser = serial.Serial('/dev/serial0', 9600, timeout=1)
    ser.write("5".encode())
    response = ""
    while response == "":
        response = ser.readline().decode()
    print(response)
    ser.close()

def encendido_cuarto ():
    # Setup
    light_cuarto_on()

def apagado_cuarto():
    light_cuarto_off()

def encendido_cocina ():
    # Setup
    light_cocina_on()

def apagado_cocina():
    light_cocina_off()

def encendido_banio():
    # Setup
    light_banio_on()

def apagado_banio():
    light_banio_off()

def puerta_up():
    door_up_gp()

def puerta_down():
    door_down_gp()

@app.route("/")
def home():
    '''
    Página de inicio de api web
    '''
    return "<h1>CASA INTELIGENTE API!</h1>"

@app.route(BASE_URL +  LIGHT + "/on" + "/<string:lugar>/",methods=['POST'])
def ligth_on(lugar):
    '''
    Encender led
    '''
    #encendido()
    if(lugar == "cuarto"):
        encendido_cuarto()
    elif(lugar == "cocina"):
        encendido_cocina()
    elif(lugar == "banio"):
        encendido_banio()
    return "OK"

@app.route(BASE_URL + LIGHT + "/off" + "/<string:lugar>/",methods=['POST'])
def ligth_off(lugar):
    '''
    Apagar led
    '''
    #apagado()
    if(lugar == "cuarto"):
        apagado_cuarto()
    elif(lugar == "cocina"):
        apagado_cocina()
    elif(lugar == "banio"):
        apagado_banio()
    return "OK"


@app.route(BASE_URL + DOOR + "/up",methods=['POST'])
def door_up():
    '''
    Apagar led
    '''
    #apagado()
    puerta_up()
    return "OK"

@app.route(BASE_URL + DOOR + "/down",methods=['POST'])
def door_down():
    '''
    Apagar led
    '''
    #apagado()
    puerta_down()
    return "OK"

@app.route(BASE_URL + LIGHT + "/low",methods=['POST'])
def ligth_low():
    '''
    Apagar led
    '''
    #apagado()
    light_arduino_low()
    return "OK"

@app.route(BASE_URL + LIGHT + "/medium",methods=['POST'])
def ligth_medium():
    '''
    Apagar led
    '''
    #apagado()
    light_arduino_medium()
    return "OK"

@app.route(BASE_URL + LIGHT + "/high",methods=['POST'])
def ligth_high():
    '''
    Apagar led
    '''
    #apagado()
    light_arduino_high()
    return "OK"

if __name__ == '__main__':
    peripheral_setup()
    app.run(debug=True, host='0.0.0.0')
