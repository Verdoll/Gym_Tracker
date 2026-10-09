import pygame
import UI_base
import text_button_logic as TB
import border_squares as BS


pygame.init()

#constans
WIDTH, HEIGHT = 1000, 700
FPS = 60
fant = pygame.font.SysFont("comicsans", 30)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gym Tracker")

clock = pygame.time.Clock()

running = True

while running:
    dt = clock.tick(FPS) / 1000 #сколько секунд прошло с прошлого кадра (?)
                                #хз надо ли ваще, если что ИСПРАВИТЬ
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update

    # Draw
    screen.fill((30, 30, 30))
    for contain in UI_base.main_screen:
        contain.draw(screen)
    for contain in UI_base.stats_screen:
        contain.draw(screen)

    pygame.display.flip()

pygame.quit()