import border_squares
import pygame
pygame.init()
font = pygame.font.SysFont('comicsans', 20)

#версия и название
current_version = '0.2'
name = 'Gym Tracker'


main_screen = []
main_text = []
stats_screen = []


Name_Data_square = border_squares.Border_square( #сверху для даты и названия
    10,
    10,
    980,
    50,
    (30,30,30),
    (220,220,220),
    25,
    3
)
main_screen.append(Name_Data_square)
#версия
version_text = font.render(f'{name} {current_version}', True, (255,255,255))
version_text_pos = (30,20)
main_text.append((version_text, version_text_pos))

#основное окно с статами стандартное
Window_of_stats = border_squares.Border_square(
    250,
    80,
    740,
    600,
    (30,30,30),
    (220,220,220),
    25,
    3
)
stats_screen.append(Window_of_stats)

