import pygame
import colors


class imageObject():
    def __init__(self, img_path, size):
        try:
            self.image = pygame.image.load(img_path)
        except pygame.error:
            print("[ERROR] Couldn't open " + img_path)
            self.image.fill(colors.GREEN)
        else:
            print("Loading... " + img_path)
        self.image = pygame.transform.scale(self.image, (size[0], size[1]))


    image = pygame.Surface(size=(0, 0))
