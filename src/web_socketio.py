from flask_socketio import Namespace, emit, send, disconnect

class DrawWebSocket(Namespace):
    player = []
    count = 0

    def on_connect(self):
        pass

    def on_disconnect(self):
        DrawWebSocket.count -= 1
        temp = {
          'playerCount': DrawWebSocket.count
        }
        send(temp, broadcast=True)
        pass
    
    def on_send_connect(self, user):
        DrawWebSocket.player.append(user)
        DrawWebSocket.count += 1
        temp = {
          'user': 'Server',
          'message': user + ' connected',
          'playerCount': DrawWebSocket.count
        }
        emit('message_data', temp, broadcast=True)

    def on_message_data(self, msg):
        emit('message_data', msg, broadcast=True)

    def on_message_draw(self, msg):
        emit('message_draw', msg, broadcast=True)