# основная информация. Константы и изменяемая
# все что касается программы напрямую Б3
class Program:
    def __init__(self):
        self.active_window = 'main'
        # main, new_workout
        self.current_version = '0.2'
        self.name = 'Gym Tracker'


    def set_active_mode(self, mode):
        self.active_window = mode
