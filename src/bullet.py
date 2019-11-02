import pygame
import config
from entity import Entity
from timer import Timer
import math


class Bullet(Entity):
    def __init__(self, rect, look_vector, id_player):
        super().__init__()
        self.image = config.ball_image
        self.look_vector = pygame.Vector2(look_vector.x, look_vector.y)
        self.rect = self.image.get_rect(center=(rect.x, rect.y))
        self.position = pygame.Vector2(rect.x, rect.y)
        self.killTimer = Timer(config.ball_spawn_time, func=self.kill)
        self.start_kill_timer()

        self.owner_id = id_player

    owner_id = 0
    last_reflective_wall_id = 0
    is_reflective = False
    is_enable = True
    kill_timer = None

    def kill(self):
        self.is_enable = False

    def is_kill_player(self, id_player):
        if self.owner_id != id_player:
            return True
        return self.is_reflective

    def start_kill_timer(self):
        if not self.killTimer.is_active:
            self.killTimer.start_timer()

    def check_for_touch(self, rect):
        is_touch = pygame.Rect.colliderect(self.rect, rect)
        return is_touch

    def check_for_touch_wall(self, rect, id, is_vertical):
        if self.last_reflective_wall_id != id:
            # check for a touch with sides of a wall
            if is_vertical:
                if self.rect.collidepoint(rect.midtop) or self.rect.collidepoint(rect.midbottom):
                    self.is_reflective = True
                    self.last_reflective_wall_id = id
                    self.look_vector = pygame.Vector2(self.look_vector.x, -self.look_vector.y)
                    return True

            if not is_vertical:
                if self.rect.collidepoint(rect.midleft) or self.rect.collidepoint(rect.midright):
                    self.is_reflective = True
                    self.last_reflective_wall_id = id
                    self.look_vector = pygame.Vector2(-self.look_vector.x, self.look_vector.y)
                    return True

            # check for a touch with other part
            if self.rect.colliderect(rect):
                self.is_reflective = True
                self.last_reflective_wall_id = id
                if is_vertical:
                    self.look_vector = pygame.Vector2(-self.look_vector.x, self.look_vector.y)
                else:
                    self.look_vector = pygame.Vector2(self.look_vector.x, -self.look_vector.y)

                return True

        return False

    def update_bullet(self):
        if 0 < self.rect.x < config.window_size[0] and 0 < self.rect.y < config.window_size[1]:  # check for leaving of the screen
            self.position += self.look_vector
            self.rect.center = self.position
        else:
            self.is_enable = False
