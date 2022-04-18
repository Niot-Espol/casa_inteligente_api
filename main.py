from flask import Flask

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
    app.run(debug=True, host='0.0.0.0')
