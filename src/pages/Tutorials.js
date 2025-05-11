import React, { useState, useEffect } from 'react';
import {
  Box,
  Container,
  Typography,
  Grid,
  Card,
  CardContent,
  CardActions,
  Button,
  Chip,
  Tabs,
  Tab,
  Paper,
} from '@mui/material';
import { Chessboard } from 'chessboardjsx';
import axios from 'axios';

interface Tutorial {
  id: number;
  title: string;
  content: string;
  difficulty: string;
  category: string;
  position_fen: string;
  moves: string;
}

const Tutorials: React.FC = () => {
  const [tutorials, setTutorials] = useState<Tutorial[]>([]);
  const [selectedTutorial, setSelectedTutorial] = useState<Tutorial | null>(null);
  const [currentPosition, setCurrentPosition] = useState('start');
  const [currentMoveIndex, setCurrentMoveIndex] = useState(0);
  const [selectedTab, setSelectedTab] = useState(0);

  useEffect(() => {
    fetchTutorials();
  }, []);

  const fetchTutorials = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/tutorials');
      setTutorials(response.data);
    } catch (error) {
      console.error('Error fetching tutorials:', error);
    }
  };

  const handleTutorialSelect = (tutorial: Tutorial) => {
    setSelectedTutorial(tutorial);
    setCurrentPosition(tutorial.position_fen);
    setCurrentMoveIndex(0);
  };

  const handleNextMove = () => {
    if (selectedTutorial && currentMoveIndex < selectedTutorial.moves.split(' ').length) {
      const moves = selectedTutorial.moves.split(' ');
      setCurrentMoveIndex(currentMoveIndex + 1);
      // Update position based on moves
      // This is a simplified version - you'll need to implement proper move handling
    }
  };

  const handlePreviousMove = () => {
    if (currentMoveIndex > 0) {
      setCurrentMoveIndex(currentMoveIndex - 1);
      // Update position based on moves
      // This is a simplified version - you'll need to implement proper move handling
    }
  };

  const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
    setSelectedTab(newValue);
  };

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty.toLowerCase()) {
      case 'beginner':
        return 'success';
      case 'intermediate':
        return 'warning';
      case 'advanced':
        return 'error';
      default:
        return 'default';
    }
  };

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Typography variant="h4" gutterBottom>
        Chess Tutorials
      </Typography>

      <Grid container spacing={3}>
        <Grid item xs={12} md={4}>
          <Paper sx={{ p: 2, maxHeight: '80vh', overflow: 'auto' }}>
            <Tabs
              value={selectedTab}
              onChange={handleTabChange}
              sx={{ mb: 2 }}
            >
              <Tab label="All" />
              <Tab label="Openings" />
              <Tab label="Middlegame" />
              <Tab label="Endgame" />
            </Tabs>

            {tutorials.map((tutorial) => (
              <Card
                key={tutorial.id}
                sx={{
                  mb: 2,
                  cursor: 'pointer',
                  '&:hover': { bgcolor: 'action.hover' },
                }}
                onClick={() => handleTutorialSelect(tutorial)}
              >
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    {tutorial.title}
                  </Typography>
                  <Box sx={{ mb: 1 }}>
                    <Chip
                      label={tutorial.difficulty}
                      color={getDifficultyColor(tutorial.difficulty)}
                      size="small"
                      sx={{ mr: 1 }}
                    />
                    <Chip
                      label={tutorial.category}
                      variant="outlined"
                      size="small"
                    />
                  </Box>
                  <Typography variant="body2" color="text.secondary">
                    {tutorial.content.substring(0, 100)}...
                  </Typography>
                </CardContent>
              </Card>
            ))}
          </Paper>
        </Grid>

        <Grid item xs={12} md={8}>
          {selectedTutorial ? (
            <Paper sx={{ p: 2 }}>
              <Typography variant="h5" gutterBottom>
                {selectedTutorial.title}
              </Typography>
              <Box sx={{ mb: 2 }}>
                <Chessboard
                  position={currentPosition}
                  boardWidth={500}
                  boardOrientation="white"
                />
              </Box>
              <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 2 }}>
                <Button
                  variant="contained"
                  onClick={handlePreviousMove}
                  disabled={currentMoveIndex === 0}
                >
                  Previous Move
                </Button>
                <Button
                  variant="contained"
                  onClick={handleNextMove}
                  disabled={currentMoveIndex >= selectedTutorial.moves.split(' ').length}
                >
                  Next Move
                </Button>
              </Box>
              <Typography variant="body1" paragraph>
                {selectedTutorial.content}
              </Typography>
            </Paper>
          ) : (
            <Paper sx={{ p: 4, textAlign: 'center' }}>
              <Typography variant="h6" color="text.secondary">
                Select a tutorial to begin learning
              </Typography>
            </Paper>
          )}
        </Grid>
      </Grid>
    </Container>
  );
};

export default Tutorials; 