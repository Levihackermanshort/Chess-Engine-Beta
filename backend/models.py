from .app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    rating = db.Column(db.Integer, default=1200)
    games_played = db.Column(db.Integer, default=0)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    draws = db.Column(db.Integer, default=0)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    white_player_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    black_player_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    result = db.Column(db.String(10))  # '1-0', '0-1', '1/2-1/2'
    moves = db.Column(db.Text)  # PGN format
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    time_control = db.Column(db.String(20))
    game_type = db.Column(db.String(20))  # 'casual', 'rated', 'tournament'

class Tutorial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String(20))  # 'beginner', 'intermediate', 'advanced'
    category = db.Column(db.String(50))  # 'openings', 'middlegame', 'endgame', etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    position_fen = db.Column(db.String(100))  # Starting position in FEN notation
    moves = db.Column(db.Text)  # PGN format of the tutorial

class TrainingExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String(20))
    category = db.Column(db.String(50))
    position_fen = db.Column(db.String(100))
    solution = db.Column(db.Text)  # PGN format of the solution
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tutorial_id = db.Column(db.Integer, db.ForeignKey('tutorial.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('training_exercise.id'))
    completed = db.Column(db.Boolean, default=False)
    score = db.Column(db.Integer)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow) 