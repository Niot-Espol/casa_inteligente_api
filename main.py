from flask import Flask
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
import serial
import sys

app = Flask(__name__)

BASE_URL = "/api"
LIGHT = "/light"


def peripheral_setup():
    GPIO.setmode(GPIO.BCM) #puede cambiar a BOARD
    global led1
    led1 = 17  #si cambiar de BCM a Board defina el número del pin acorde a los pines de la raspberry
    GPIO.setup(led1, GPIO.OUT)

def light_On():
    GPIO.output(led1,True)

def light_Off():
    GPIO.output(led1,False)

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

def encendido () :
    # Setup
    peripheral_setup()
    light_On()

def apagado():
    peripheral_setup()
    light_Off()

@app.route("/")
def home():
    '''
    Página de inicio de api web
    '''
    return "<h1>CASA INTELIGENTE API!</h1>"

@app.route(BASE_URL + LIGHT + "/on",methods=['POST'])
def ligth_on():
    '''
    Encender led
    '''
    #encendido()
    light_arduino_on()
    print("loading")
    return "OK"

@app.route(BASE_URL + LIGHT + "/off",methods=['POST'])
def ligth_off():
    '''
    Apagar led
    '''
    #apagado()
    light_arduino_off()
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

