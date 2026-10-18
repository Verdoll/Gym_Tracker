import border_squares
import Buttons
import Color_pallete as pallete
import pygame
import Program
pygame.init()
font = pygame.font.SysFont('comicsans', 20)

#версия и название
current_version = Program.current_version
name = Program.name


main_screen = []
main_buttons = []
main_text = []
stats_screen = []
new_workout_screen = []
new_workout_buttons = []
window_of_activity = []
choice_activity = []
window_1 = [window_of_activity, choice_activity]

def drawing(screen):
    for contain in main_screen:
        contain.draw(screen)

    for text in main_text:
        screen.blit(text[0], text[1])

    for button in main_buttons:
        button.draw(screen)




Name_Data_square = border_squares.Border_square( #сверху для даты и названия
    10,
    10,
    980,
    50,
    pallete.background,
    pallete.white,
    25,
    3
)
main_screen.append(Name_Data_square)
New_Workout = Buttons.Button(
    10,
    80,
    230,
    50,
    pallete.background,
    pallete.white,
    25,
    3,
    font.render('Новая тренировка', True, (255,255,255)),
    pallete.active_color_buttons,
    'new_workout'
)
main_buttons.append(New_Workout)
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
    pallete.background,
    pallete.white,
    25,
    3
)
stats_screen.append(Window_of_stats)

###   new workout   ###
main_frame_new_workout = border_squares.Border_square(
    250,
    80,
    740,
    600,
    pallete.background,
    pallete.white,
    25,
    3
)
new_workout_screen.append(main_frame_new_workout)

#new_activity
Frame_activity_window = border_squares.Border_square(
    270,
    150,
    300,
    400,
    pallete.background,
    pallete.white,
    10,
    3
)
window_of_activity.append(Frame_activity_window)


#buttons on new_workout
Button_choice_new_workout = Buttons.Button_with_choice(
    270,
    100,
    300,
50,
    pallete.background,
    pallete.white,
    10,
    3,
    font.render('                                       \/', True, (255,255,255)),
    pallete.active_color_buttons,
    None,
    window_1,
)
new_workout_buttons.append(Button_choice_new_workout)



###############################################
#              NEW ACTIVITYS                  #
###############################################
PullUps_activity = Buttons.Additional_Button(
    270,
    150,
    300,
    50,
    pallete.background,
    pallete.white,
    10,
    3,
    font.render('Подтягивания', True, (255,255,255)),
    pallete.active_color_buttons,
    None,
)
choice_activity.append(PullUps_activity)

Bench_Press = Buttons.Additional_Button(
    270,
    200,
    300,
    50,
    pallete.background,
    pallete.white,
    10,
    3,
    font.render('Жим лежа', True, (255,255,255)),
    pallete.active_color_buttons,
    None,
)
choice_activity.append(Bench_Press)

Biceps = Buttons.Additional_Button(
    270,
    250,
    300,
    50,
    pallete.background,
    pallete.white,
    10,
    3,
    font.render('Бицепс', True, (255,255,255)),
    pallete.active_color_buttons,
    None,
)
choice_activity.append(Biceps)

Triceps = Buttons.Additional_Button(
    270,
    300,
    300,
    50,
    pallete.background,
    pallete.white,
    10,
    3,
    font.render('Трицепс', True, (255,255,255)),
    pallete.active_color_buttons,
    None,
)
choice_activity.append(Triceps)

Seated_row = Buttons.Additional_Button(
    270,
    350,
    300,
    50,
    pallete.background,
    pallete.white,
    10,
    3,
    font.render('Горизонтальная тяга', True, (255,255,255)),
    pallete.active_color_buttons,
    None,
)
choice_activity.append(Seated_row)

Dumbbell_lateral_raises = Buttons.Additional_Button(
    270,
    400,
    300,
    50,
    pallete.background,
    pallete.white,
    10,
    3,
    font.render('Подъем гантелей в стороны', True, (255,255,255)),
    pallete.active_color_buttons,
    None,
)
choice_activity.append(Dumbbell_lateral_raises)

