from flask import Flask, request
import socket

app = Flask(__name__)

# Agregamos una variable global para llevar el conteo de accesos
access_count = 0

@app.route('/')
def index():
    return 'Practica1 - creacion de una APIUrequest!'

@app.route('/holamundo/')
def holamundo():
    return 'HOLA MUNDO'

@app.route('/pruebadocker/')
def holadocker():
    return 'HOLA DOCKER'

@app.route('/nginx/')
def nginx():
    return '<body bgcolor=ff0000> <h1>ENDPOINT ACTIVADO NGINx!<H1> <body>'

# Agregamos un nuevo endpoint llamado '/nuevoendpoint/' que muestra el contador y el hostname
@app.route('/nuevoendpoint/')
def nuevoendpoint():
    global access_count
    access_count += 1
    hostname = socket.gethostname()
    return f'You clicked this page {access_count} times on server: {hostname}'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)