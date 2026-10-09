import border_squares

main_screen = []
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

