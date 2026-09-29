import pygame
import text_button_logic as TB


pygame.init()

#constans
WIDTH, HEIGHT = 1000, 700
FPS = 60
fant = pygame.font.SysFont("comicsans", 30)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gym Tracker")

clock = pygame.time.Clock()

test_button = TB.TextButton(100,
                            100,
                            100,
                            100,
                            (255,255,255),
                            'df324s',
                            pygame.font.SysFont("comicsans", 30),
                            (255, 0, 0),
                            120,
                            120)

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
    test_button.draw_button(screen)

    pygame.display.flip()

pygame.quit()