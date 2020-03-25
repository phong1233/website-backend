from .models import Leaderboard, Score
import json

class Service():
    @staticmethod
    def get_all_leaderboard():
        leaderboard = Leaderboard.objects()
        json_lead = leaderboard.to_json()
        dicts = json.loads(json_lead)
        return dicts
    
    @staticmethod
    def add_new_score(game, score, user):
        leaderboard = Leaderboard.objects(game=game).first()
        new_score = Score(user=user, score=score)
        if leaderboard is None:
            new_lead = Leaderboard(game=game, leaderboard=[new_score])
            new_lead.save()
        else:
            leaderboard.leaderboard.append(new_score)
            leaderboard.save()
        new_leaderboard = Leaderboard.objects(game=game).first()
        json_lead = new_leaderboard.to_json()
        dicts = json.loads(json_lead)
        return dicts['leaderboard']
    
    @staticmethod
    def get_leaderboard(game):
        new_leaderboard = Leaderboard.objects(game=game).first()
        if(new_leaderboard is None):
            new_lead = Leaderboard(game=game)
            new_lead.save()
            new_leaderboard = new_lead
        json_lead = new_leaderboard.to_json()
        dicts = json.loads(json_lead)
        return dicts['leaderboard']
