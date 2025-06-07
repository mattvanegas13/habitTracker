from flask import Blueprint

habits_bp = Blueprint('habits_bp', __name__)

@habits_bp.route('/', methods=['GET', 'POST'])
def habits():
    return 'Habits'

@habits_bp.route('/<id>/check-ins', methods=['POST'])
def check_in(id):
    return 'Check In'

@habits_bp.route('/<id>/streaks', methods=['GET'])
def streaks(id):
    return 'Streaks'
