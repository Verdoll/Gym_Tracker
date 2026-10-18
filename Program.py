# основная информация. Константы и изменяемая
# все что касается программы напрямую Б3
current_version = '0.3'
name = 'Gym Tracker'
name_window = 'Gym Tracker'


class Program:
    def __init__(self):
        self.active_window = 'main'
        # main, new_workout
        self.current_version = current_version
        self.name = name
        self.name_window = name_window
        self.DEBUG = True


    def set_active_mode(self, mode):
        self.active_window = mode
