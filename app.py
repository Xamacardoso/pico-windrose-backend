from flask import Flask, request # Bibliotecas para funcionamento geral do backend
from flask_socketio import SocketIO       # Biblioteca para websocket com o frontend
from flask_cors import CORS
import time                               # Manipulação de data/hora

app = Flask(__name__)
CORS(app)
socket = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

@app.route("/update", methods=["POST"])
def update_data():
    data = request.json
    data["timestamp"] = time.strftime("%H:%M:%S", time.localtime()) + " GMT (Londres)"
    print(f"[RECEBIDO]: {data}")

    # Envio via websocket
    socket.emit('update', data)
    return {"status": "ok"}, 200

if __name__ == '__main__':
    socket.run(app, host="0.0.0.0", port=5000)