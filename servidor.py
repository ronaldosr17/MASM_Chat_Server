import os
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
