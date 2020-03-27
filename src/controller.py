from flask import Blueprint, jsonify, request
from src.services import Service


simple_page = Blueprint('simple_page', __name__)

@simple_page.route('/', methods=['GET'])
def default_page():
    return 'Hello world!'

@simple_page.route('/leaderboard', methods=['GET'])
def get_all_leaderboards():
    lead = Service.get_all_leaderboard()
    return {'result': lead}

@simple_page.route('/leaderboard/<game>', methods=['POST'])
def post_new_leaderboard(game):
    body = request.get_json()
    lead = Service.add_new_score(**body, game=game)
    return jsonify({'leaderboard': lead})

@simple_page.route('/leaderboard/<game>', methods=['GET'])
def get_leaderboard(game):
    lead = Service.get_leaderboard(game=game)
    return jsonify({'leaderboard': lead})