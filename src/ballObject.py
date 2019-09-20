import pygame
import config
from entityObject import entityObject
from imageObject import imageObject


class ballObject(pygame.sprite.Sprite):
    def __init__(self, rect, lookAtVector):
        super().__init__()
        self.image = config.ball_image
        self.lookAtVector = pygame.Vector2(lookAtVector.x, lookAtVector.y)
        self.rect = self.image.get_rect(center=(rect.x, rect.y))

    def checkForToutch(self, rect):
        isToutch = pygame.Rect.colliderect(self.rect, rect)
        if isToutch:
            self.isEnable = False
        return isToutch

    def updateBall(self):
        if self.rect.x > 0 and self.rect.x < config.window_size[0] and self.rect.y > 0 and self.rect.y < config.window_size[1]:
            self.rect = self.rect.move(self.lookAtVector.x, self.lookAtVector.y)
        else:
            self.isEnable = False

    isEnable = True


