import pygame
import sys

pygame.init()

grid_size = 4
tile_size = 100
grid_margin = 10
screen_width = grid_size * tile_size + (grid_size + 1) * grid_margin
screen_height = grid_size * tile_size + (grid_size + 1) * grid_margin
bg_white = (255, 255, 255)
bg_black = (0, 0, 0)

screen = pygame.display.set_mode((screen_width, screen_height))

def draw_text(text, col, row):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(
        (grid_margin + tile_size) * col + grid_margin + tile_size // 2,
        (grid_margin + tile_size) * row + grid_margin + tile_size // 2
    ))
    screen.blit(text_surface, text_rect)

def draw_grid():
    numbers = [2**i for i in range(1, grid_size**2 + 1) if 2**i <= 2048]
    count = 0
    for row in range(grid_size):
        for col in range(grid_size):
            pygame.draw.rect(screen, bg_white, [
                (grid_margin + tile_size) * col + grid_margin,
                (grid_margin + tile_size) * row + grid_margin,
                tile_size,
                tile_size
            ])
            if count < len(numbers):
                draw_text(str(numbers[count]), col, row)
                count += 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_black)
    draw_grid()
    pygame.display.flip()
