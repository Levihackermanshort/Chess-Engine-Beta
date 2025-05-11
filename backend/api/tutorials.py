from flask import Blueprint, request, jsonify
from ..models import Tutorial, db

tutorials_bp = Blueprint('tutorials', __name__)

@tutorials_bp.route('/', methods=['GET'])
def get_tutorials():
    try:
        category = request.args.get('category')
        difficulty = request.args.get('difficulty')
        
        query = Tutorial.query
        
        if category:
            query = query.filter_by(category=category)
        if difficulty:
            query = query.filter_by(difficulty=difficulty)
            
        tutorials = query.all()
        
        return jsonify([{
            'id': t.id,
            'title': t.title,
            'content': t.content,
            'difficulty': t.difficulty,
            'category': t.category,
            'position_fen': t.position_fen,
            'moves': t.moves,
            'created_at': t.created_at.isoformat()
        } for t in tutorials])
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@tutorials_bp.route('/<int:tutorial_id>', methods=['GET'])
def get_tutorial(tutorial_id):
    try:
        tutorial = Tutorial.query.get_or_404(tutorial_id)
        return jsonify({
            'id': tutorial.id,
            'title': tutorial.title,
            'content': tutorial.content,
            'difficulty': tutorial.difficulty,
            'category': tutorial.category,
            'position_fen': tutorial.position_fen,
            'moves': tutorial.moves,
            'created_at': tutorial.created_at.isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@tutorials_bp.route('/', methods=['POST'])
def create_tutorial():
    try:
        data = request.get_json()
        
        required_fields = ['title', 'content', 'difficulty', 'category', 'position_fen', 'moves']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        tutorial = Tutorial(
            title=data['title'],
            content=data['content'],
            difficulty=data['difficulty'],
            category=data['category'],
            position_fen=data['position_fen'],
            moves=data['moves']
        )
        
        db.session.add(tutorial)
        db.session.commit()
        
        return jsonify({
            'id': tutorial.id,
            'title': tutorial.title,
            'content': tutorial.content,
            'difficulty': tutorial.difficulty,
            'category': tutorial.category,
            'position_fen': tutorial.position_fen,
            'moves': tutorial.moves,
            'created_at': tutorial.created_at.isoformat()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@tutorials_bp.route('/<int:tutorial_id>', methods=['PUT'])
def update_tutorial(tutorial_id):
    try:
        tutorial = Tutorial.query.get_or_404(tutorial_id)
        data = request.get_json()
        
        for field in ['title', 'content', 'difficulty', 'category', 'position_fen', 'moves']:
            if field in data:
                setattr(tutorial, field, data[field])
        
        db.session.commit()
        
        return jsonify({
            'id': tutorial.id,
            'title': tutorial.title,
            'content': tutorial.content,
            'difficulty': tutorial.difficulty,
            'category': tutorial.category,
            'position_fen': tutorial.position_fen,
            'moves': tutorial.moves,
            'created_at': tutorial.created_at.isoformat()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@tutorials_bp.route('/<int:tutorial_id>', methods=['DELETE'])
def delete_tutorial(tutorial_id):
    try:
        tutorial = Tutorial.query.get_or_404(tutorial_id)
        db.session.delete(tutorial)
        db.session.commit()
        return '', 204
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500 