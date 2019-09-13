import pygame
import config
from ballObject import ballObject
from entityObject import entityObject


class playerObject(entityObject):
    def __init__(self, rect, imgPATH):
        super().__init__()
        try:
            self.__original_image = pygame.image.load(imgPATH).convert_alpha()
        except pygame.error:
            print("ERROR PYGAME " + imgPATH)
            exit(-1)
        else:
            print("Loading... " + imgPATH)
            self.__original_image = pygame.transform.scale(self.__original_image, (rect.width, rect.height))
            self.image = self.__original_image.copy()
            self.image = pygame.transform.rotate(self.__original_image, self.angle)
            self.lookAtVector = pygame.Vector2(-self.currentSpeed, 0)
            self.position = pygame.Vector2(rect.x, rect.y)
            self.rect = self.image.get_rect(center=self.position)


    angleSpeed = 3
    angle = 90
    __original_image = 0
    image = 0
    balls = []
    isAlive = True

    def addBall(self):
        if len(self.balls) < 5:
            self.balls.append(ballObject(pygame.Rect(self.get_barrel_end().x, self.get_barrel_end().y, 5, 5), pygame.Vector2(self.lookAtVector.x, self.lookAtVector.y)))

    def get_barrel_end(self):
        return self.rect.center + pygame.math.Vector2(0, -self.rect.height//2 - 10).rotate(-self.angle)

    def setAngle(self, value):
        self.angle += value
        self.lookAtVector.rotate_ip(-value)
        self.image = pygame.transform.rotate(self.__original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def movePlayerForward(self):
        self.position += self.lookAtVector
        self.rect.center = self.position

    def movePlayerBack(self):
        self.position -= self.lookAtVector
        self.rect.center = self.position

    def movePlayerLeft(self):
        self.setAngle(self.angleSpeed)

    def movePlayerRight(self):
        self.setAngle(-self.angleSpeed)
