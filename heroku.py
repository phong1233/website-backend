from flask import Flask
from flask_mongoengine import MongoEngine
from flask_socketio import SocketIO
from flask_cors import CORS
from src.controller import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)
CORS(app)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://website-backend:m9tUkzFzZx0e5wLl@ds247690.mlab.com:47690/heroku_lbqvnqd4',
    'retryWrites': 'false'
}
db = MongoEngine()
db.init_app(app)
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app, debug=True)