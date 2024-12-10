# Sudoku Solver with Animation

### Overview
The following program will implement a Sudoku Solver algorithm that allows the user to choose a difficulty level for a Sudoku Puzzle and solve that given puzzle while following Sudoku's rules. The program will use a recursive backtracking algorithm in order to fill in the empty slots and test the valid numbers step-by-step; the solving process is visualized through an animated Pygame interface.


### Features
- Will solve Sudoku Puzzles of varying difficulty; in this case, we decided to include easy, medium, hard, and extreme.
- It will visualize the backtracking algorithm in real-time using a Pygame animation.
- Provides a user-friendly terminal interface when initially selecting the Sudoku Puzzle modes.


## How It Works:
- The user will select a Sudoku Puzzle mode.
- The program will validate the given input from the user and initialize the puzzle; it will display to the user the "Selected Sudoku Puzzle".
- A recursive backtracking algorithm will solve the given Sudoku puzzle where the numbers will be tested based on Sudoku's rules.
- An animated board will update to show the algorithm's progress; once solved the animated board will close and a completed board - "Solved Sudoku Puzzle" - will be displayed in the terminal.


## How To Run:
- Clone/download the contents provided/in this repository.
- Please ensure you have the following below installed before running the provided program:
    - Pygame library
    - Python 3.6+
- Run the program titled "sudoku_solver_with_viz".
- Follow the on-screen instructions to select a Sudoku Puzzle mode (easy, medium, hard, extreme).


## Acknowledgments
This project was developed as part of the Algoithm Design & Analysis Final Project by:
- Kelly A. Lozano Analco
- Jimwell Marigmen
- Elisa Avalos

## References
- Textbook: The Algorithm Design Manual (2nd Edition) by Steven S. Skiena
- Python Documentation: docs.python.org
- Pygame Documentation: pygame.org/docs
