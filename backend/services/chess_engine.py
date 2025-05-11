import chess
import chess.engine
from typing import Tuple, Optional
import random
from collections import defaultdict

class ChessEngine:
    def __init__(self, skill_level: int = 20):
        """
        Initialize the chess engine with a pure Python implementation.
        skill_level: 0-20, where 20 is the strongest
        """
        self.skill_level = min(max(skill_level, 0), 20)
        self.piece_values = {
            chess.PAWN: 100,
            chess.KNIGHT: 320,
            chess.BISHOP: 330,
            chess.ROOK: 500,
            chess.QUEEN: 900,
            chess.KING: 20000
        }
        
    def evaluate_position(self, board: chess.Board) -> int:
        """
        Evaluate the current position.
        Positive value means white is winning, negative means black is winning.
        """
        score = 0
        
        # Material score
        for piece_type in chess.PIECE_TYPES:
            score += len(board.pieces(piece_type, chess.WHITE)) * self.piece_values[piece_type]
            score -= len(board.pieces(piece_type, chess.BLACK)) * self.piece_values[piece_type]
        
        # Checkmate and stalemate
        if board.is_checkmate():
            return 1000000 if board.turn == chess.BLACK else -1000000
        if board.is_stalemate():
            return 0
        
        return score

    def get_best_move(self, fen: str, difficulty: int = 10) -> dict:
        """
        Get the best move for the current position.
        """
        board = chess.Board(fen)
        
        # Reduce search depth based on difficulty
        max_depth = min(4, difficulty // 2)
        
        # Simple minimax search with alpha-beta pruning
        best_move = None
        best_score = float('-inf')
        
        for move in board.legal_moves:
            board.push(move)
            score = -self.minimax(board, max_depth - 1, float('-inf'), float('inf'))
            board.pop()
            
            if score > best_score:
                best_score = score
                best_move = move
        
        if best_move:
            return {
                'from': chess.square_name(best_move.from_square),
                'to': chess.square_name(best_move.to_square),
                'promotion': chess.PIECE_SYMBOLS[best_move.promotion] if best_move.promotion else None,
                'san': board.san(best_move)
            }
        
        return {'error': 'No legal moves available'}

    def minimax(self, board: chess.Board, depth: int, alpha: float, beta: float) -> float:
        """
        Minimax search with alpha-beta pruning.
        """
        if depth == 0 or board.is_game_over():
            return self.evaluate_position(board)
        
        if board.turn == chess.WHITE:
            max_eval = float('-inf')
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, alpha, beta)
                board.pop()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, alpha, beta)
                board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def get_move_suggestions(self, fen: str) -> list:
        """
        Get a list of suggested moves with their evaluations.
        """
        board = chess.Board(fen)
        suggestions = []
        
        for move in board.legal_moves:
            board.push(move)
            score = self.evaluate_position(board)
            board.pop()
            
            suggestions.append({
                'move': {
                    'from': chess.square_name(move.from_square),
                    'to': chess.square_name(move.to_square),
                    'promotion': chess.PIECE_SYMBOLS[move.promotion] if move.promotion else None,
                    'san': board.san(move)
                },
                'score': score
            })
        
        # Sort suggestions by score
        suggestions.sort(key=lambda x: x['score'], reverse=board.turn == chess.WHITE)
        return suggestions

    def is_checkmate(self, board: chess.Board) -> bool:
        """
        Check if the current position is checkmate.
        """
        return board.is_checkmate()

    def is_stalemate(self, board: chess.Board) -> bool:
        """
        Check if the current position is stalemate.
        """
        return board.is_stalemate()

    def is_insufficient_material(self, board: chess.Board) -> bool:
        """
        Check if there is insufficient material to checkmate.
        """
        return board.is_insufficient_material()

    def get_fen(self, board: chess.Board) -> str:
        """
        Get the FEN string representation of the current position.
        """
        return board.fen()

    def get_pgn(self, board: chess.Board) -> str:
        """
        Get the PGN string representation of the game.
        """
        return board.pgn()