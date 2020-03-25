from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
from src.models import Leaderboard, Score
from src.services import Service

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'websiteBackend',
    'host': 'mongodb://localhost:27017/websiteDB'
}
#hi
db = MongoEngine()
db.init_app(app)

@app.route('/', methods=['GET'])
def default_page():
    return 'Hello world!'

@app.route('/leaderboard', methods=['GET'])
def get_all_leaderboards():
    lead = Service.get_all_leaderboard()
    return {'result': lead}

@app.route('/leaderboard/<game>', methods=['POST'])
def post_new_leaderboard(game):
    body = request.get_json()
    lead = Service.add_new_score(**body, game=game)
    return jsonify({'leaderboard': lead})

@app.route('/leaderboard/<game>', methods=['GET'])
def get_leaderboard(game):
    lead = Service.get_leaderboard(game=game)
    return jsonify({'leaderboard': lead})

if __name__ == '__main__':
    app.run(debug=True)

