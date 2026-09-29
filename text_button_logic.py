import pygame
import Universal_object
pygame.init()

#ребенок универсального класса, для ввода текста. Впервые трогаю наследование
class TextButton(Universal_object.Object):
    def __init__(self, x, y, width, height, color, text, font, text_color, x_pos_txt, y_pos_txt):
        Universal_object.Object.__init__(self, x, y, width, height, color)
        self.text = text
        self.font = font
        self.text_color = text_color
        self.x_pos_txt = x_pos_txt
        self.y_pos_txt = y_pos_txt


    def draw_text(self, screen):
        text_surface = self.font.render(self.text, True, self.text_color)
        screen.blit(text_surface, (self.x_pos_txt, self.y_pos_txt))



    def draw_button(self, screen):
        self.draw(screen)
        self.draw_text(screen)


    def update_text(self, text):
        self.text = text


    def is_active(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True


