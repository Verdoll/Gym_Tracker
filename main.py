import pygame
import Program
import UI_base
import Color_pallete as pallete
import text_button_logic as TB
import border_squares as BS


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
            for button in UI_base.main_buttons:
                button.check_click(x,y, program)
            for button in UI_base.new_workout_buttons:
                button.check_click(x,y, program)
            if UI_base.new_workout_buttons[0].is_active:
                for button in UI_base.window_1[1]:
                    button.check_click(x,y, UI_base.Button_choice_new_workout)

                if program.DEBUG:
                    print(button.is_active, program.active_window)

    # Update

    # Draw
    screen.fill(pallete.background)
    UI_base.drawing(screen)

    if program.active_window == 'main':
        for contain in UI_base.stats_screen:
            contain.draw(screen)

    if program.active_window == 'new_workout':
        for contain in UI_base.new_workout_screen:
            contain.draw(screen)
        for contain in UI_base.new_workout_buttons:
            contain.draw(screen)

    pygame.display.flip()

pygame.quit()