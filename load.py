import os
import pygame

class Load:
    def __init__(self):
        pygame.init()
        self.file = os.path.dirname(__file__)
        self.graphic = os.path.join(self.file, 'graphics')

        self.img_cache = {}

    def summon_img(self, surface=None,  postion = (0, 0), name: str=None, convert_alpha: bool=False, rect : bool=False):
        if surface is None:
            surface = pygame.display.get_surface()

        if name in self.img_cache:
            return self.img_cache[name]

        path = os.path.join(self.graphic, name)
        if convert_alpha:
            img = pygame.image.load(path).convert_alpha()
            img_rect = img.get_rect(topleft=(postion))
        else:
            img = pygame.image.load(path)
            img_rect = img.get_rect(topleft=(postion))

        self.img_cache[name] = img

        surface.blit(img, img_rect.topleft)

        return img_rect