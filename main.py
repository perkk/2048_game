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

grid = [[0] * grid_size for _ in range(grid_size)]
score = 0

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

def insert_rand_tile():
    empty_positions = [(i, j) for i in range(grid_size) for j in range(grid_size) if grid[i][j] == 0]

    if empty_positions:
        i, j = random.choice(empty_positions)
        grid[i][j] = random.choice([2, 4])

def move_up():
    for col in range(grid_size):
        values = [grid[row][col] for row in range(grid_size) if grid[row][col] != 0]
        values += [0] * (grid_size - len(values))
        for row in range(grid_size):
            grid[row][col] = values[row]

def move_down():
    for col in range(grid_size):
        values = [grid[row][col] for row in range(grid_size) if grid[row][col] != 0]
        values = [0] * (grid_size - len(values)) + values
        for row in range(grid_size):
            grid[row][col] = values[row]


def move_left():
    for row in range(grid_size):
        values = [val for val in grid[row] if val != 0]
        values += [0] * (grid_size - len(values))
        grid[row][:] = values

def move_right():
    for row in range(grid_size):
        values = [val for val in reversed(grid[row]) if val != 0]
        values += [0] * (grid_size - len(values))
        grid[row][:] = list(reversed(values))

def handle_input_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up()
            elif event.key == pygame.K_DOWN:
                move_down()
            elif event.key == pygame.K_LEFT:
                move_left()
            elif event.key == pygame.K_RIGHT:
                move_right()

insert_rand_tile()
insert_rand_tile()

while True:
    handle_input_events()
    screen.fill(bg_black)
    draw_grid()
    pygame.display.flip()
