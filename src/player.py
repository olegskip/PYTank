import pygame
from bullet import Bullet
from image import Image
from entity import Entity
from levels_manager import *
from gif import Gif


class Player(Entity):
    def __init__(self, rect, imgPATH, id):
        super().__init__()
        self.__original_image = Image(imgPATH, size=(rect.width, rect.height)).image.convert_alpha()

        self.bullets = []
        self.distance_vector = pygame.Vector2(0, 0)
        self.safe_bullet_distance = 0
        self.bullet_speed = 10

        self.look_vector_bullet = pygame.Vector2(-7, 0)
        self.angle_speed = 3
        self.angle = 90

        self.victory_points = 0
        self.is_alive = True
        self.death_gif = Gif(config.PATH_TO_EFFECTS + "\\smoke\\frames\\", [70, 70], 0.02)
        self.id = id

        self.current_speed = 10
        self.position = pygame.Vector2()
        self.look_vector = pygame.Vector2()
        self.rect = pygame.Rect(0, 0, 0, 0)

        self.spawn()
        self.set_rect(rect)
        self.mask = pygame.mask.from_surface(self.__original_image)
        self.image_rect = self.image.get_rect()

    image_rect = None
    __original_image = None
    image = None

    bullets = []
    distance_vector = None
    safe_bullet_distance = 0
    bullet_speed = 10

    look_vector_bullet = None
    angle_speed = 3
    angle = 90

    victory_points = 0
    is_alive = True
    death_gif = None
    id = 0

    mask = None

    def reset(self):
        self.victory_points = 0
        if self.death_gif:
            self.death_gif.stop()

    def spawn(self):
        self.image = self.__original_image.copy()
        self.angle = 0
        self.set_angle(0)
        self.look_vector = pygame.Vector2(-self.current_speed, 0)
        self.look_vector_bullet = pygame.Vector2(-self.bullet_speed, 0)
        self.is_alive = True
        self.bullets.clear()
        if self.death_gif:
            self.death_gif.stop()

    def set_image(self, img_path):
        self.__original_image = Image(img_path, size=(self.__original_image.get_rect().width, self.__original_image.get_rect().height)).image.convert_alpha()
        self.image = pygame.transform.rotate(self.__original_image, self.angle)

    def set_position(self, x, y):
        self.set_rect(self.image.get_rect(center=(x, y)))

    def set_rect(self, rect):
        self.rect = self.image.get_rect(center=(rect.x, rect.y))
        self.position = pygame.Vector2(rect.x, rect.y)
        self.distance_vector = pygame.math.Vector2(0, -(self.rect.height + self.safe_bullet_distance) // 2)

    def set_save_distance(self, distance):
        self.safe_bullet_distance = distance
        self.distance_vector = pygame.math.Vector2(0, -(self.rect.height + self.safe_bullet_distance) // 2)

    def get_barrel_end(self):
        return self.rect.center + self.distance_vector.rotate(-self.angle)

    def set_speed(self, speed, bullet_speed):
        self.current_speed = speed
        self.bullet_speed = bullet_speed
        self.look_vector = pygame.Vector2(-self.current_speed, 0)
        self.look_vector_bullet = pygame.Vector2(-self.bullet_speed, 0)

    def add_bullet(self):
        if len(self.bullets) < config.max_ball_count and self.is_alive:
            self.bullets.append(Bullet(pygame.Rect(self.get_barrel_end().x + config.ball_radius // 2,
                                                   self.get_barrel_end().y, config.ball_radius, config.ball_radius),
                                       self.look_vector_bullet, self.id))

    def kill(self):
        self.is_alive = False
        self.death_gif.start_drawing()

    def check_for_leave_of_screen(self):
        width, height = config.window_size

        # height - y
        if self.rect.top < 0 or self.rect.bottom < 0 and self.look_vector.y < 0:
            self.rect.top = 0
            self.position = pygame.Vector2(self.rect.center)
        elif self.rect.bottom > height or self.rect.top > height and self.look_vector.y > 0:
            self.rect.bottom = height
            self.position = pygame.Vector2(self.rect.center)
        # width - x
        if self.rect.left < 0 or self.rect.right < 0 and self.look_vector.x < 0:
            self.rect.left = 0
            self.position = pygame.Vector2(self.rect.center)
        elif self.rect.right > width or self.rect.left > width and self.look_vector.x > 0:
            self.rect.right = width
            self.position = pygame.Vector2(self.rect.center)

    def wall_collision_angle_handler(self, value):
        angle = self.angle + value * 2
        look_vector = pygame.Vector2(*self.look_vector)
        look_vector.rotate_ip(-value)
        image = pygame.transform.rotate(self.__original_image, angle)

        temp_rect = self.rect
        temp_rect = image.get_rect(center=temp_rect.center)

        for wall in lvlManager.levels[lvlManager.current_level_index].walls:
            offset = (int(temp_rect.topleft[0] - wall.rect.x), int(temp_rect.topleft[1] - wall.rect.y))
            result = wall.mask.overlap(self.mask, offset)
            if result:
                return result
        return False

    def wall_collision_handler(self, value):
        self.mask = pygame.mask.from_surface(self.image)

        topleft = self.rect.topleft + value
        for wall in lvlManager.levels[lvlManager.current_level_index].walls:
            offset = (int(topleft[0] - wall.rect.x), int(topleft[1] - wall.rect.y))
            result = wall.mask.overlap(self.mask, offset)
            if result:
                return True
        return False

    def set_angle(self, value):
        self.angle += value
        self.look_vector.rotate_ip(-value)
        self.look_vector_bullet.rotate_ip(-value)
        self.image = pygame.transform.rotate(self.__original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.check_for_leave_of_screen()

    def move_forward(self):
        if self.is_alive and not self.wall_collision_handler(self.look_vector):
            self.position += self.look_vector
            self.rect.center = self.position

    def move_back(self):
        if self.is_alive and not self.wall_collision_handler(-self.look_vector):
            self.position -= self.look_vector
            self.rect.center = self.position

    def move_left(self):
        if self.is_alive and not self.wall_collision_angle_handler(self.angle_speed):
            self.set_angle(self.angle_speed)

    def move_right(self):
        if self.is_alive and not self.wall_collision_angle_handler(-self.angle_speed):
            self.set_angle(-self.angle_speed)
