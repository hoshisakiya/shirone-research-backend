from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from source.api.read_book import read_book_bp

app = Flask(__name__)
app.register_blueprint(read_book_bp, url_prefix='/read_book')
CORS(app, cors_allowed_origins="*")
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def handle_message(data):
    emit('message', data)
    return


def run() -> int:
    app.run(host="localhost", port=5000)
    socketio.run(app)
    return 0
