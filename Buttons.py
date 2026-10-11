import border_squares
import pygame
pygame.init()

class Button(border_squares.Border_square):

    def __init__(self, x, y, width, height, color, color_sides, border_radius, sides_width, text, text_position, active_color,
                 mode):
        border_squares.Border_square.__init__(self, x, y, width, height, color, color_sides, border_radius, sides_width)
        self.text = text
        self.text_position = text_position
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




