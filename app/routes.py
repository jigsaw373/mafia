# app/routes.py

from flask import Blueprint, request, jsonify, current_app
from .zoom import get_zoom_client
from .logic import assign_roles, roles

main = Blueprint('main', __name__)


def get_meeting_participants(client, meeting_id):
    response = client.meeting.get(id=meeting_id)
    participants = response.json().get('participants', [])
    return [p['id'] for p in participants]


def send_private_message(client, participant_id, message):
    client.chat.send(user_id=participant_id, message=message)


@main.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})


@main.route('/start_game', methods=['POST'])
def start_game():
    meeting_id = request.json.get('meeting_id')
    with current_app.app_context():
        client = get_zoom_client()
        participants = get_meeting_participants(client, meeting_id)
        if len(participants) < len(roles):
            return jsonify({"error": "Not enough participants for the game"}), 400
        assigned_roles = assign_roles(participants)
        for participant_id, role in assigned_roles.items():
            send_private_message(client, participant_id, f"Your role is: {role}")
        return jsonify({"message": "Game started!"})


@main.route('/player_action', methods=['POST'])
def player_action():
    player_id = request.json.get('player_id')
    action = request.json.get('action')
    # Process player action (this part would need further implementation based on game logic)
    return jsonify({"message": "Action received"})
