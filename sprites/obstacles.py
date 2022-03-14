import os
import random
import pygame


class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        images = ['largecactus1.png', 'largecactus2.png', 'largecactus3.png',
                  'smallcactus1.png', 'smallcactus2.png', 'smallcactus3.png']
        image = os.path.join(r'assets\images', random.choice(images))
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()
        self.rect.bottomleft = (surface.get_width(), surface.get_rect().centery)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= 5

        if self.rect.right < 0:
            self.kill()
