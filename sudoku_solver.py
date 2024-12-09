#Name: Kelly A. Lozano Analco, Jimwell Marigmen, Elisa Avalos

#COMP 221 Final Project

#The following below will allow the user to choose a puzzle mode and solve the puzzle while adhering to the given rules of Sudoku.
#It will implement a recursive backtracking algorithm to efficiently solve the puzzle; it will test the valid numbers for the empty slots on the board.
#An animation will be shown to the user in order to demonstrate the backtracking algorithm.

#Acknowledgements: Used the COMP 221 textbook; The Algorithm Design Manual 2nd Edition by Steven S. Skiena
#Acknowledgements: Used the Python Documentation ('https://docs.python.org/3/') for help.
#Acknowledgements: Used the Pygame Documentation (https://www.pygame.org/docs/) for help.


import pygame
import time

pygame.init()

SCREEN_SIZE = 540
GRID_SIZE = SCREEN_SIZE // 9
FONT = pygame.font.Font(None, 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
RED = (255, 50, 50)

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Sudoku Solver Animation")


def draw_board(board, highlight = None):
    """
    The following below will draw the Sudoku Puzzle board with a Pygame screen.
    Creates a 9x9 board; will add additional digits to the board given the mode selected by the user.

    :param board: A 2D list that will represent the Sudoku Puzzle board.
    :param highlight: Tuples (row, col) of the squares on the Sudoku Puzzle board that will highlight the progress.
    """
    screen.fill(WHITE)

    for i in range(10):
        line_width = 3 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (0, i * GRID_SIZE), (SCREEN_SIZE, i * GRID_SIZE), line_width)
        pygame.draw.line(screen, BLACK, (i * GRID_SIZE, 0), (i * GRID_SIZE, SCREEN_SIZE), line_width)

    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                color = BLUE if highlight == (row, col) else BLACK
                text = FONT.render(str(board[row][col]), True, color)
                screen.blit(text, (col * GRID_SIZE + GRID_SIZE // 3, row * GRID_SIZE + GRID_SIZE // 4))
    pygame.display.update()


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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        draw_board(board, (row, col))
                        time.sleep(0.02)

                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                        draw_board(board, (row, col))
                        time.sleep(0.02)
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
            [0, 0, 0, 0, 0, 0, 0, 4, 9],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 8, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [7, 0, 0, 0, 5, 0, 0, 0, 0]
        ]
    elif mode == 'medium':
        return [
            [0, 0, 0, 0, 0, 0, 0, 1, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 6, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 7, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 5],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [3, 4, 0, 0, 0, 0, 0, 0, 0]
        ]
    elif mode == 'hard':
        return [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    elif mode == 'extreme':
        return [
            [0 for _ in range(9)] for _ in range(9)
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