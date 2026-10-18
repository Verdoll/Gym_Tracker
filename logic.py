import UI_base

def buttons_update(x, y, program):
    for button in UI_base.main_buttons:
        button.check_click(x, y, program)
    for button in UI_base.new_workout_buttons:
        button.check_click(x, y, program)
    if UI_base.new_workout_buttons[0].is_active:
        for button in UI_base.window_1[1]:
            button.check_click(x, y, UI_base.Button_choice_new_workout)


def draw_ui(screen, program):
    if program.active_window == 'main':
        for contain in UI_base.stats_screen:
            contain.draw(screen)

    if program.active_window == 'new_workout':
        for contain in UI_base.new_workout_screen:
            contain.draw(screen)
        for contain in UI_base.new_workout_buttons:
            contain.draw(screen)