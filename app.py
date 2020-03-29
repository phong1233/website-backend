import os
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_socketio import SocketIO
from flask_cors import CORS
from src.controller import simple_page
from src.web_socketio import DrawWebSocket

app = Flask(__name__)
app.register_blueprint(simple_page)
CORS(app)
app.config['MONGODB_SETTINGS'] = {
    'host': os.environ['MONGODB_URI'],
    'retryWrites': 'false'
}
db = MongoEngine()
db.init_app(app)
socketio = SocketIO(app, cors_allowed_origins='https://www.phonglehigh.tech')

socketio.on_namespace(DrawWebSocket('/draw'))

if __name__ == '__main__':
    socketio.run(app, debug=True)