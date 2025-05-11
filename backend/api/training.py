from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

training_bp = Blueprint('training', __name__)

@training_bp.route('/exercises', methods=['GET'])
@jwt_required()
def get_exercises():
    # TODO: Implement exercise retrieval logic
    exercises = [
        {
            'id': 1,
            'title': 'Basic Chess Rules',
            'description': 'Learn the basic rules of chess',
            'difficulty': 'beginner'
        },
        {
            'id': 2,
            'title': 'Opening Principles',
            'description': 'Learn basic opening principles',
            'difficulty': 'intermediate'
        }
    ]
    return jsonify(exercises), 200

@training_bp.route('/exercise/<int:exercise_id>', methods=['GET'])
@jwt_required()
def get_exercise(exercise_id):
    # TODO: Implement exercise retrieval by ID
    return jsonify({'message': f'Exercise {exercise_id} details'}), 200
