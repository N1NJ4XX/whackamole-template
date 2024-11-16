import pygame
import random

GRID_WIDTH = 20
GRID_HEIGHT = 16
TILE_SIZE = 32
WINDOW_WIDTH = GRID_WIDTH * TILE_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * TILE_SIZE

def draw_grid(screen):
    for x in range(0, WINDOW_WIDTH, TILE_SIZE):
        pygame.draw.line(screen, "black", (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, "black", (0, y), (WINDOW_WIDTH, y))

def get_random_position():
    grid_x = random.randrange(0, GRID_WIDTH) * TILE_SIZE
    grid_y = random.randrange(0, GRID_HEIGHT) * TILE_SIZE
    return grid_x, grid_y

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Whack-a-mole")
    clock = pygame.time.Clock()

    mole_image = pygame.image.load("mole.png")
    mole_position = (0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                mole_rect = pygame.Rect(mole_position[0], mole_position[1], TILE_SIZE, TILE_SIZE)

                if mole_rect.collidepoint(mouse_x, mouse_y):
                    mole_position = get_random_position()

        screen.fill("light green")
        draw_grid(screen)
        screen.blit(mole_image, mole_position)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
