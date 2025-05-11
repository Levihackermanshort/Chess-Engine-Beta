# Chess Engine
![Uploading Chess Engine Web May 11, 2025, 04_49_29 PM.png…]()

A modern web-based chess application featuring an AI-powered chess engine, interactive tutorials, and user authentication.

## Features

- 🎮 Play chess against an AI opponent powered by Stockfish
- 📚 Interactive chess tutorials and lessons
- 👤 User authentication and profile management
- 🎨 Multiple chess piece sets and board themes
- 📱 Responsive design for desktop and mobile
- 🔍 Move validation and legal move highlighting
- 📊 Game history and statistics tracking

## Tech Stack

### Backend
- Python/Flask
- SQLite Database
- Stockfish Chess Engine
- Flask-SQLAlchemy for ORM
- Flask-JWT-Extended for authentication
- Flask-Migrate for database migrations

### Frontend
- React with TypeScript
- React Chessboard
- Tailwind CSS for styling
- React Router for navigation
- Axios for API calls

## Prerequisites

- Python 3.8+
- Node.js 14+
- Stockfish Chess Engine
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Levihackermanshort/chess-engine.git
cd chess-engine
```

2. Set up the backend:
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Initialize the database
flask db init
flask db migrate
flask db upgrade
```

3. Set up the frontend:
```bash
cd frontend
npm install
```

4. Create a `.env` file in the root directory with the following variables:
```
FLASK_APP=backend/app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here
DATABASE_URL=sqlite:///chess.db
STOCKFISH_PATH=path/to/stockfish
```

## Running the Application

1. Start the backend server:
```bash
flask run
```

2. In a new terminal, start the frontend development server:
```bash
cd frontend
npm start
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## Project Structure

```
chess-engine/
├── backend/
│   ├── api/
│   │   ├── auth.py
│   │   ├── games.py
│   │   └── tutorials.py
│   ├── models/
│   │   ├── user.py
│   │   ├── game.py
│   │   └── tutorial.py
│   ├── services/
│   │   └── chess_engine.py
│   └── app.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.tsx
│   └── package.json
├── requirements.txt
└── README.md
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Stockfish Chess Engine](https://stockfishchess.org/)
- [React Chessboard](https://github.com/Clariity/react-chessboard)
- [Python Chess](https://github.com/niklasf/python-chess) 
