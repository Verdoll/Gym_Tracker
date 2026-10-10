import border_squares
import pygame
pygame.init()

class Button(border_squares.Border_square):

    def __init__(self, x, y, width, height, color_fill, color_sides, border_radius, sides_width, text, text_position, active_color):
        border_squares.Border_square.__init__(self, x, y, width, height, color_fill, color_sides, border_radius, sides_width)
        self.text = text
        self.text_position = text_position
        self.active_color = active_color
        self.disactive_color = color_fill
        self.is_active = False


    def swap_mode(self):
        self.is_active = not self.is_active
        if self.is_active:
            self.color_fill = self.active_color
        else:
            self.color_fill = self.disactive_color


    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            self.rect,
            border_radius=self.border_radius,
        )

        pygame.draw.rect(
            screen,
            self.color_sides,
            self.rect,
            width=self.sides_width,
             border_radius=self.border_radius
        )

        screen.blit(self.text, self.text_position)


    def check_mode(self):
        if self.is_active:
            self.color_fill = self.active_color
        else:
            self.color_fill = self.disactive_color




