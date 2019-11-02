import pygame


class Entity:
    def __init__(self):
        self.current_speed = 10
        self.position = pygame.Vector2()
        self.look_vector = pygame.Vector2()
        self.rect = pygame.Rect(0, 0, 0, 0)

    current_speed = 0
    position = None
    look_vector = None
    rect = None
