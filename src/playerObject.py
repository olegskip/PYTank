import pygame
import config
from ballObject import ballObject
from imageObject import imageObject
from entityObject import entityObject


class playerObject(entityObject):
    def __init__(self, rect, imgPATH):
        super().__init__()
        self.__original_image = imageObject(imgPATH, size=(rect.width, rect.height)).image.convert_alpha()
        self.image = self.__original_image.copy()
        self.image = pygame.transform.rotate(self.__original_image, self.angle)
        self.lookAtVector = pygame.Vector2(-self.currentSpeed, 0)
        self.lookAtVectorBullet = pygame.Vector2(-self.bulletSpeed, 0)
        self.rect = self.image.get_rect(center=(rect.x, rect.y))
        self.position = pygame.Vector2(rect.x, rect.y)
        self.distance_vector = pygame.math.Vector2(0, -self.rect.height // 2)


    distance_vector = pygame.Vector2(0, 0)
    bulletSpeed = 10
    lookAtVectorBullet = pygame.Vector2(-7, 0)
    angleSpeed = 3
    angle = 90
    __original_image = 0
    image = 0
    balls = []
    isAlive = True

    def checkForLeaveOfScreen(self):
        width, height = config.window_size

        if self.rect.top < 0 or self.rect.bottom < 0 and self.lookAtVector.y < 0:
            self.rect.top = 0
            self.position = pygame.Vector2(self.rect.center)
        elif self.rect.bottom > height or self.rect.top > height and self.lookAtVector.y > 0:
            self.rect.bottom = height
            self.position = pygame.Vector2(self.rect.center)
        if self.rect.left < 0 or self.rect.right < 0 and self.lookAtVector.x < 0:
            self.rect.left = 0
            self.position = pygame.Vector2(self.rect.center)
        elif self.rect.right > width or self.rect.left > width and self.lookAtVector.x > 0:
            self.rect.right = width
            self.position = pygame.Vector2(self.rect.center)

    def setSaveDistance(self, distance):
        self.distance_vector = pygame.math.Vector2(0, -(self.rect.height + distance) // 2)

    def get_barrel_end(self):
        return self.rect.center + self.distance_vector.rotate(-self.angle)

    def setSpeed(self, speed, bulletSpeed):
        self.currentSpeed = speed
        self.bulletSpeed = bulletSpeed
        self.lookAtVector = pygame.Vector2(-self.currentSpeed, 0)
        self.lookAtVectorBullet = pygame.Vector2(-self.bulletSpeed, 0)

    def addBall(self):
        if len(self.balls) < 5 and self.isAlive:
            self.balls.append(ballObject(pygame.Rect(self.get_barrel_end().x + config.ball_radius // 2, self.get_barrel_end().y, config.ball_radius, config.ball_radius), self.lookAtVectorBullet))

    def kill(self):
        self.isAlive = False

    def setAngle(self, value):
        self.angle += value
        self.lookAtVector.rotate_ip(-value)
        self.lookAtVectorBullet.rotate_ip(-value)
        self.image = pygame.transform.rotate(self.__original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.checkForLeaveOfScreen()

    def movePlayerForward(self):
        self.position += self.lookAtVector
        self.rect.center = self.position
        self.checkForLeaveOfScreen()

    def movePlayerBack(self):
        self.position -= self.lookAtVector
        self.rect.center = self.position
        self.checkForLeaveOfScreen()

    def movePlayerLeft(self):
        self.setAngle(self.angleSpeed)

    def movePlayerRight(self):
        self.setAngle(-self.angleSpeed)
