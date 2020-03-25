import mongoengine

class Score(mongoengine.EmbeddedDocument):
    user = mongoengine.StringField(required=True, max_length=7)
    score = mongoengine.IntField(required=True)

class Leaderboard(mongoengine.Document):
    game = mongoengine.StringField(required=True)
    leaderboard = mongoengine.SortedListField(mongoengine.EmbeddedDocumentField(Score), ordering="score", reverse=True, default=[])
