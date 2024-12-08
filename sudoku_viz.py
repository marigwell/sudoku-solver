import pygame

pygame.init()

width, height = 600, 600
grid_size = 9
cell_width = width // grid_size
cell_height = height // grid_size

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sudoku Solver using Backtracking')

# colors that will be used
WHITE = (255, 255, 255)
LIGHT_DARK = (50, 50, 50)
THICK_LINE_COLOR = (0, 0, 0)  # darker lines for the 3x3 subgrids

def draw_grid():
    """ Draws out the 9x9 sudoku grid"""
    for row in range(grid_size):
        for col in range(grid_size):
            pygame.draw.rect(screen, LIGHT_DARK, (col * cell_width, row * cell_height, cell_width, cell_height), 1)
    
    for row in range(0, grid_size, 3):
        for col in range(0, grid_size, 3):
            pygame.draw.rect(screen, THICK_LINE_COLOR, (col * cell_width, row * cell_height, 3 * cell_width, 3 * cell_height), 4)

def main():
	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False


		screen.fill(WHITE)

		draw_grid()
		pygame.display.flip()

main()
pygame.quit()
