import pygame


class Wall:
    def __init__(self, start_pos, end_pos, is_vertical, id):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.is_vertical = is_vertical
        self.id = id

    def set_up_init_params(self, rect, surface):
        self.rect = rect
        self.mask = pygame.mask.from_surface(surface.convert_alpha())

    id = 0
    start_pos = (0, 0)
    end_pos = (0, 0)
    rect = pygame.Rect(0, 0, 0, 0)

    is_vertical = False
    mask = None
    surface = None
