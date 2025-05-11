import React, { useState, useEffect } from 'react';
import { Chess } from 'chess.js';
import { Chessboard } from 'chessboardjsx';
import {
  Box,
  Paper,
  Typography,
  Button,
  Slider,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Grid,
} from '@mui/material';
import axios from 'axios';

const Game: React.FC = () => {
  const [game, setGame] = useState(new Chess());
  const [position, setPosition] = useState('start');
  const [difficulty, setDifficulty] = useState(10);
  const [gameStatus, setGameStatus] = useState('');
  const [moveHistory, setMoveHistory] = useState<string[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const makeMove = async (move: any) => {
    try {
      setIsLoading(true);
      const gameCopy = new Chess(game.fen());
      const result = gameCopy.move(move);
      
      if (!result) {
        throw new Error('Invalid move');
      }

      setGame(gameCopy);
      setPosition(gameCopy.fen());
      setMoveHistory(prev => [...prev, result.san]);
      
      // Check game status
      if (gameCopy.isCheckmate()) {
        setGameStatus('Checkmate!');
        return;
      } else if (gameCopy.isDraw()) {
        setGameStatus('Draw!');
        return;
      } else if (gameCopy.isCheck()) {
        setGameStatus('Check!');
      } else {
        setGameStatus('');
      }

      // Get AI move
      try {
        const response = await axios.post('http://localhost:5000/api/chess/move', {
          fen: gameCopy.fen(),
          difficulty: difficulty,
        });

        const aiMove = response.data.move;
        if (!gameCopy.move(aiMove)) {
          throw new Error('Invalid AI move');
        }
        
        setGame(gameCopy);
        setPosition(gameCopy.fen());
        setMoveHistory(prev => [...prev, aiMove.san]);
      } catch (error) {
        console.error('Error getting AI move:', error);
        setGameStatus('Error getting AI move');
      }
    } catch (error) {
      console.error('Error making move:', error);
      setError(error instanceof Error ? error.message : 'Invalid move');
    } finally {
      setIsLoading(false);
    }
  };

  const onDrop = (move: any) => {
    const sourceSquare = move.sourceSquare;
    const targetSquare = move.targetSquare;
    const moveObj = {
      from: sourceSquare,
      to: targetSquare,
      promotion: 'q', // Always promote to queen for simplicity
    };
    makeMove(moveObj);
  };

  const resetGame = () => {
    const newGame = new Chess();
    setGame(newGame);
    setPosition('start');
    setGameStatus('');
    setMoveHistory([]);
  };

  return (
    <Box sx={{ p: 3 }}>
      <Grid container spacing={3}>
        <Grid item xs={12} md={8}>
          <Paper sx={{ p: 2 }}>
            <Chessboard
              position={position}
              onPieceDrop={onDrop}
              boardWidth={600}
              boardOrientation="white"
            />
          </Paper>
        </Grid>
        <Grid item xs={12} md={4}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Game Controls
            </Typography>
            <Box sx={{ mb: 3 }}>
              <Typography gutterBottom>AI Difficulty</Typography>
              <Slider
                value={difficulty}
                onChange={(_, value) => setDifficulty(value as number)}
                min={1}
                max={20}
                marks
                valueLabelDisplay="auto"
              />
            </Box>
            <Button
              variant="contained"
              color="primary"
              onClick={resetGame}
              fullWidth
              sx={{ mb: 2 }}
            >
              New Game
            </Button>
            {gameStatus && (
              <Typography
                variant="h6"
                color="primary"
                sx={{ textAlign: 'center', mb: 2 }}
              >
                {gameStatus}
              </Typography>
            )}
            <Typography variant="h6" gutterBottom>
              Move History
            </Typography>
            <Box sx={{ maxHeight: 300, overflow: 'auto' }}>
              {moveHistory.map((move, index) => (
                <Typography key={index}>
                  {Math.floor(index / 2) + 1}.
                  {index % 2 === 0 ? ' ' : '...'} {move}
                </Typography>
              ))}
            </Box>
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
};

export default Game; 