from flask import Blueprint, request, jsonify
from ..services.chess_engine import ChessEngine
import chess

chess_bp = Blueprint('chess', __name__)
engine = ChessEngine()

@chess_bp.route('/move', methods=['POST'])
def make_move():
    try:
        data = request.get_json()
        fen = data.get('fen')
        difficulty = data.get('difficulty', 10)
        
        if not fen:
            return jsonify({'error': 'FEN string is required'}), 400
        
        move = engine.get_best_move(fen, difficulty)
        return jsonify({'move': move})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chess_bp.route('/evaluate', methods=['GET'])
def evaluate_position():
    try:
        fen = request.args.get('fen')
        if not fen:
            return jsonify({'error': 'FEN string is required'}), 400
        
        evaluation = engine.evaluate_position(fen)
        return jsonify(evaluation)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chess_bp.route('/suggest', methods=['GET'])
def get_move_suggestions():
    try:
        fen = request.args.get('fen')
        if not fen:
            return jsonify({'error': 'FEN string is required'}), 400
        
        suggestions = engine.get_move_suggestions(fen)
        return jsonify(suggestions)
    except Exception as e:
        return jsonify({'error': str(e)}), 500