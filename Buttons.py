import border_squares
import pygame
pygame.init()

class Button(border_squares.Border_square):

    def __init__(self, x, y, width, height, color, color_sides, border_radius, sides_width, text, active_color,
                 mode):
        border_squares.Border_square.__init__(self, x, y, width, height, color, color_sides, border_radius, sides_width)
        self.text = text
        self.active_color = active_color
        self.disactive_color = color
        self.is_active = False
        self.mode = mode



    def swap_mode(self, program):
        self.is_active = not self.is_active
        if self.is_active:
            self.color = self.active_color
            program.active_window = self.mode
        else:
            self.color = self.disactive_color
            program.active_window = 'main'




    def draw(self, screen):
        super().draw(screen)

        rect = self.text.get_rect(
            center=(self.x + self.width // 2, self.y + self.height // 2)
        )
        screen.blit(self.text, rect)


    def check_mode(self):
        if self.is_active:
            self.color = self.active_color
        else:
            self.color = self.disactive_color


    def check_click(self, x, y, program):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            self.swap_mode(program)



class Button_with_choice(Button):
    def __init__(self, x, y, width, height, color, color_sides, border_radius, sides_width, text, active_color, mode, window):
        Button.__init__(self, x, y, width, height, color, color_sides, border_radius, sides_width, text, active_color, mode)
        self.is_active = False
        self.window = window
        self.common_text = '                                       \/'


    def swap_mode(self):
        self.is_active = not self.is_active
        if self.is_active:
            self.color = self.active_color
        else:
            self.color = self.disactive_color


    def check_click(self, x, y, program):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            self.swap_mode()


    def new_text(self, text):
        self.text = text


    def draw(self, screen):
        super().draw(screen)
        if self.is_active:
            for lists in self.window:
                for contain in lists:
                    contain.draw(screen)


class Additional_Button(Button):
    def __init__(self, x, y, width, height, color, color_sides, border_radius, sides_width, text, active_color, mode):
        Button.__init__(self, x, y, width, height, color, color_sides, border_radius, sides_width, text, active_color, mode)


    def click(self, main_button):
        main_button.text = self.text
        main_button.color = main_button.disactive_color
        main_button.is_active = False


    def check_click(self, x, y, main_button):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            self.click(main_button)



