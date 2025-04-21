from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

mensajes = []

@app.route('/api/mensaje', methods=['POST'])
def recibir():
    data = request.json
    mensajes.append(data)
    return {"status": "mensaje recibido"}

@app.route('/api/mensajes', methods=['GET'])
def obtener():
    return {"mensajes": mensajes}

if __name__ == '__main__':
    app.run()
