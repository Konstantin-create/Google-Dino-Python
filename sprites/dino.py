import pygame


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_run1 = pygame.image.load(r"assets\images\dinorun1.png")
        self.image_run2 = pygame.image.load(r"assets\images\dinorun2.png")
        self.image = self.image_run1
        self.rect = self.image.get_rect()

        surface = pygame.display.get_surface()
        self.rect.center = (surface.get_rect().centerx // 4, surface.get_rect().centery - 25)
        self.step = 0
        self.jumping = False
        self.height = 15
        self.sound_jump = pygame.mixer.Sound(r"assets\sounds\jump.wav")

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.step += 1
        if self.step % 7 == 0:
            if self.image == self.image_run1:
                self.image = self.image_run2
            else:
                self.image = self.image_run1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jumping:
            self.jumping = True
            self.sound_jump.play()
        if self.jumping:
            self.jump()

    def jump(self):
        self.rect.y -= self.height
        self.height -= 1
        if self.height < -15:
            self.height = 15
            self.jumping = False
