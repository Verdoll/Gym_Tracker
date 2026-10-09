import border_squares
class Button(border_squares):
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


