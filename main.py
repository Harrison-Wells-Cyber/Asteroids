import pygame
from circleshape import CircleShape
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from constants import ASTEROID_KINDS
from constants import ASTEROID_MAX_RADIUS
from constants import ASTEROID_MIN_RADIUS
from constants import ASTEROID_SPAWN_RATE_SECONDS
from asteroidfield import AsteroidField
from logger import log_event
import sys
from shot import Shot
from constants import PLAYER_SHOOT_SPEED

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    clock = pygame.time.Clock()
    dt = 0.0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return
        screen.fill("Black")
        for thing in drawable:
            thing.draw(screen)
        updatable.update(dt)
        for rock in asteroids:
            bool = CircleShape.collides_with(rock, player1)
            if bool == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for rock in asteroids:
            for bullet in shots:
                bool1 = CircleShape.collides_with(rock, bullet)
                if bool1 == True:
                    log_event("asteroid_shot")
                    rock.split()
                    bullet.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
