import pygame
from sprites.road import Road
from sprites.cloud import Cloud
from sprites.dino import Dino
from sprites.obstacles import Obstacles
from sprites.score import Score
import sys

pygame.init()

# Константы/Constants
WIDTH = 700
HEIGHT = 500
FPS = 60

# Создание окна/Window creating
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino")
clock = pygame.time.Clock()


def main():
    # Спрайты/Sprites
    road = Road()
    clouds = pygame.sprite.Group()
    player = Dino()
    obstacles = pygame.sprite.Group()
    score = Score()

    running = True
    while running:
        # Частота обновления экрана/Screen refresh rate
        clock.tick(FPS)

        # События/Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for obstacle in obstacles:
            if pygame.sprite.collide_mask(player, obstacle):
                sound_die = pygame.mixer.Sound(r"assets\sounds\die.wav")
                sound_die.play()
                main()

        # Рендеринг/Rendering
        screen.fill((255, 255, 255))
        road.draw(screen)
        clouds.draw(screen)
        player.draw(screen)
        obstacles.draw(screen)
        score.draw(screen)

        # Обновление спрайтов/Updating sprites
        road.update()
        clouds.update()
        if len(clouds) < 3:
            cloud = Cloud()
            clouds.add(cloud)
        player.update()
        obstacles.update()
        if len(obstacles) < 1:
            obstacle = Obstacles()
            obstacles.add(obstacle)
        score.update()

        # Обновление экрана/Screen Refresh
        pygame.display.update()


if __name__ == "__main__":
    main()
