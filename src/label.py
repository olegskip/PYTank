import pygame


class Label:
    def __init__(self, text, font_name, font_size, font_color, background_color=None):
        try:
            pygame.font.Font(font_name, font_size)
        except FileNotFoundError:
            print("[ERROR] Couldn't open " + font_name)
            temp_font = pygame.font.SysFont("Times New Roman", font_size)
        else:
            print("Loading... " + font_name)
            temp_font = pygame.font.Font(font_name, font_size)

        self.current_color = font_color
        self.current_background_color = background_color
        self.current_font = temp_font
        self.text_obj = self.current_font.render(text, False, self.current_color, self.current_background_color)

    def set_text(self, text):
        self.text_obj = self.current_font.render(text, False, self.current_color, self.current_background_color)

    is_show = False
    current_color = None
    current_background_color = None
    current_font = None
    text_obj = None
