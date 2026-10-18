import pygame
import Program
import UI_base
import Color_pallete as pallete
import logic


pygame.init()

program = Program.Program()

#constans
WIDTH, HEIGHT = 1000, 700
FPS = 60
fant = pygame.font.SysFont("comicsans", 30)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(Program.name_window)

clock = pygame.time.Clock()

running = True

while running:
    dt = clock.tick(FPS) / 1000 #сколько секунд прошло с прошлого кадра (?)
                                #хз надо ли ваще, если что ИСПРАВИТЬ

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if program.DEBUG:
                print('1', x,y)
            logic.buttons_update(x, y, program)

    # Update

    # Draw
    screen.fill(pallete.background)
    UI_base.drawing(screen)

    logic.draw_ui(screen, program)

    pygame.display.flip()

pygame.quit()