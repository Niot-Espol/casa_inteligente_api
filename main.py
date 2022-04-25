from flask import Flask
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

app = Flask(__name__)

BASE_URL = "/api"
LIGHT = "/light"

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
    #DO IT STUFF
    print("loading")
    return "OK"

@app.route(BASE_URL + LIGHT + "/off",methods=['POST'])
def ligth_off():
    '''
    Apagar led
    '''
    #DO IT STUFF
    return "OK"

if __name__ == '__main__':
    main()
    app.run(debug=True, host='0.0.0.0')

def peripheral_setup():
    GPIO.setmode(GPIO.BCM) #puede cambiar a BOARD
    global led1
    led1 = 17  #si cambiar de BCM a Board defina el número del pin acorde a los pines de la raspberry
    GPIO.setup(led1, GPIO.OUT)

def peripheral_loop():
    GPIO.output(led1,True)
    sleep(2)
    GPIO.output(led1,False)
    sleep(2)

def main () :
    # Setup
    peripheral_setup()
    # Infinite loop
    while 1 :
        peripheral_loop()

