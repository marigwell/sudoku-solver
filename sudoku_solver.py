#Name: Kelly A. Lozano Analco, Jimwell Marigmen, Elisa Avalos

#COMP 221 Final Project

#The following below will allow the user to choose a puzzle mode and solve the puzzle while adhering to the given rules of Sudoku.
#It will implement a recursive backtracking algorithm to efficiently solve the puzzle; it will test the valid numbers for the empty slots on the board.

#Acknowledgements: Used the COMP 221 textbook; The Algorithm Design Manual 2nd Edition by Steven S. Skiena
#Acknowledgements: Used the Python Documentation ('https://docs.python.org/3/') for help.
#Acknowledgements: Used the Pygame Documentation (https://www.pygame.org/docs/) for help.


def is_valid(board, row, col, num):
    "The following below will check if placing a given number on the board would be valid according to the Sudoku rules."
    if num in board[row]:
        return False

    if num in [board[i][col] for i in range(9)]:
        return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    "The following below will solve the Sudoku Puzzle using backtracking."
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def print_board(board):
    "The following will print the Sudoku board in a readable format."
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


def get_puzzle(mode):
    "The following below will return the Sudoku Puzzle based on the user's selected mode."
    if mode == 'easy':
        return [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
    elif mode == 'medium':
        return [
            [0, 0, 0, 6, 0, 0, 4, 0, 0],
            [7, 0, 0, 0, 0, 3, 6, 0, 0],
            [0, 0, 0, 0, 9, 1, 0, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 0, 1, 8, 0, 0, 0, 3],
            [0, 0, 0, 3, 0, 6, 0, 4, 5],
            [0, 4, 0, 2, 0, 0, 0, 6, 0],
            [9, 0, 3, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 1, 0, 0]
        ]
    elif mode == 'hard':
        return [
            [8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 6, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 9, 0, 2, 0, 0],
            [0, 5, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 4, 5, 7, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 0, 0, 6, 8],
            [0, 0, 8, 5, 0, 0, 0, 1, 0],
            [0, 9, 0, 0, 0, 0, 4, 0, 0]
        ]
    elif mode == 'extreme':
        return [
            [0, 0, 0, 0, 0, 0, 0, 1, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 6, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 7, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 5],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 4, 0, 0, 0, 0, 0, 0, 0]
        ]
    else:
        raise ValueError("Invalid entry! Please try again.")


def main():
    print("Choose a Sudoku Puzzle mode: 'easy', 'medium', 'hard', 'extreme'")
    mode = input("Please type the selected mode and hit 'enter': ").lower()
    try:
        puzzle = get_puzzle(mode)
        print("\nSelected Sudoku Puzzle:")
        print_board(puzzle)

        if solve_sudoku(puzzle):
            print("\nSolved Sudoku Puzzle:")
            print_board(puzzle)
        else:
            print("\nNo solution exists for the selected Sudoku Puzzle.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()