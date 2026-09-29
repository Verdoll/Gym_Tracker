import pygame
import text_button_logic as TB


pygame.init()

#constans
WIDTH, HEIGHT = 1000, 700
FPS = 60

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

    pygame.display.flip()

pygame.quit()