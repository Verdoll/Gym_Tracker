import pygame
import Universal_object
pygame.init()

#ребенок универсального класса, для ввода текста. Впервые трогаю наследование
class TextButton(Universal_object.Object):
    def __init__(self, x, y, width, height, color, text, font):
        Universal_object.Object.__init__(self, x, y, width, height, color)
        self.text = text
        self.font = font