import pygame
import colors


class Image():
    def __init__(self, img_path=None, size=None):
        self.image.fill(colors.GREEN)
        if img_path:
            try:
                self.image = pygame.image.load(img_path).convert_alpha()
            except pygame.error:
                print("[ERROR] Couldn't open " + img_path)
                self.image.fill(colors.GREEN)
            else:
                print("Loading... " + img_path)
            self.image = pygame.transform.scale(self.image, (size[0], size[1]))

    image = pygame.Surface(size=(0, 0))
