import pygame
import sys
import random

pygame.init()

grid_size = 4
tile_size = 100
grid_margin = 10
screen_width = grid_size * tile_size + (grid_size + 1) * grid_margin
screen_height = grid_size * tile_size + (grid_size + 1) * grid_margin
bg_white = (255, 255, 255)
bg_black = (0, 0, 0)

screen = pygame.display.set_mode((screen_width, screen_height))

# Initialize the game grid with zeros
grid = [[0] * grid_size for _ in range(grid_size)]

def draw_text(text, col, row):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(
        (grid_margin + tile_size) * col + grid_margin + tile_size // 2,
        (grid_margin + tile_size) * row + grid_margin + tile_size // 2
    ))
    screen.blit(text_surface, text_rect)

def draw_grid():
    for row in range(grid_size):
        for col in range(grid_size):
            pygame.draw.rect(screen, bg_white, [
                (grid_margin + tile_size) * col + grid_margin,
                (grid_margin + tile_size) * row + grid_margin,
                tile_size,
                tile_size
            ])
            if grid[row][col] != 0:
                draw_text(str(grid[row][col]), col, row)

def insert_random_tile():
    # Get a list of empty positions
    empty_positions = [(i, j) for i in range(grid_size) for j in range(grid_size) if grid[i][j] == 0]

    if empty_positions:
        # Choose a random empty position
        i, j = random.choice(empty_positions)
        # Place a 2 or 4 at the chosen position
        grid[i][j] = random.choice([2, 4])

def move(direction):
    # Transpose the grid if moving left or right to make the logic uniform
    if direction in ('left', 'right'):
        grid[:] = [list(row) for row in zip(*grid)]

    for row in range(grid_size):
        # Move non-zero values to the farthest possible position
        values = [val for val in grid[row] if val != 0]
        values += [0] * (grid_size - len(values))
        # Merge adjacent equal values
        for i in range(grid_size - 1):
            if values[i] == values[i + 1]:
                values[i], values[i + 1] = 2 * values[i], 0
        # Move non-zero values to the farthest possible position after merging
        values = [val for val in values if val != 0]
        values += [0] * (grid_size - len(values))
        grid[row][:] = values

    # Transpose the grid back to its original state if necessary
    if direction in ('left', 'right'):
        grid[:] = [list(row) for row in zip(*grid)]

def slide_tiles(direction):
    # Move tiles in the specified direction
    if direction == 'left':
        for row in range(grid_size):
            values = [val for val in grid[row] if val != 0]
            values += [0] * (grid_size - len(values))
            grid[row][:] = values
    elif direction == 'right':
        for row in range(grid_size):
            values = [val for val in reversed(grid[row]) if val != 0]
            values += [0] * (grid_size - len(values))
            grid[row][:] = list(reversed(values))
    elif direction == 'up':
        for col in range(grid_size):
            values = [grid[row][col] for row in range(grid_size) if grid[row][col] != 0]
            values += [0] * (grid_size - len(values))
            for row in range(grid_size):
                grid[row][col] = values[row]
    elif direction == 'down':
        for col in range(grid_size):
            values = [grid[row][col] for row in reversed(range(grid_size)) if grid[row][col] != 0]
            values += [0] * (grid_size - len(values))
            for row in range(grid_size):
                grid[row][col] = values[row]

def handle_input_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                slide_tiles('left')
                move('left')
                insert_random_tile()
            elif event.key == pygame.K_RIGHT:
                slide_tiles('right')
                move('right')
                insert_random_tile()
            elif event.key == pygame.K_UP:
                slide_tiles('up')
                move('up')
                insert_random_tile()
            elif event.key == pygame.K_DOWN:
                slide_tiles('down')
                move('down')
                insert_random_tile()

# Insert two random tiles at the beginning
insert_random_tile()
insert_random_tile()

while True:
    handle_input_events()
    screen.fill(bg_black)
    draw_grid()
    pygame.display.flip()
