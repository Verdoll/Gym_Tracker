import Universal_object
import pygame

class Border_square(Universal_object.Object):
    def __init__(self, x, y, width, height, color_fill, color_sides, border_radius, sides_width):
        Universal_object.Object.__init__(self, x, y, width, height, color_fill)
        self.color_sides = color_sides
        self.border_radius = border_radius
        self.sides_width = sides_width
        self.rect = (self.x, self.y, self.width, self.height)

#draw border square with filling
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

