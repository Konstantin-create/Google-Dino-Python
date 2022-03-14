import pygame


class Road(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets\images\road.png")
        self.rect = self.image.get_rect()
        self.image1 = pygame.image.load(r"assets\images\road.png")
        self.rect1 = self.image1.get_rect()

        surface = pygame.display.get_surface()
        self.rect.midleft = surface.get_rect().midleft
        self.rect1.midleft = surface.get_rect().midright

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.image, self.rect1)

    def update(self):
        self.rect.x -= 5
        self.rect1.x -= 5
        if self.rect.right < 0:
            self.rect.left = self.rect1.right
        elif self.rect1.right < 0:
            self.rect1.left = self.rect.right
