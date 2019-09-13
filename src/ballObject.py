import pygame
import config
from entityObject import entityObject


class ballObject(entityObject):
    def __init__(self, rect, lookAtVector):
        super().__init__()
        try:
            self.image = pygame.image.load(config.PATH_TO_IMAGES + '\\ball.png')
        except pygame.error:
            print("ERROR PYGAME " + config.PATH_TO_IMAGES + "\\ball.png")
            exit(-1)
        else:
            print("Loading... " + config.PATH_TO_IMAGES + "\\ball.png")

        self.image = pygame.transform.scale(self.image, (rect.height, rect.width))
        self.rect = self.image.get_rect()
        self.lookAtVector = lookAtVector
        self.position = pygame.Vector2(rect.x, rect.y)
        self.rect = self.image.get_rect(center=self.position)


    def updateBall(self):
        if self.rect.x > 0 and self.rect.x < config.window_size[0] and self.rect.y > 0 and self.rect.y < config.window_size[1]:
            self.position += self.lookAtVector
            self.rect.center = self.position
        else:
            self.isEnable = False

    isEnable = True


