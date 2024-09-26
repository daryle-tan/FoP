import pygame
import sys
from space_ship import SpaceShip
from bullet import Bullet

class Game:
    
    def __init__(self):
        #Create the main window
        pygame.init()
        self._display = pygame.display.set_mode((800,800))
        self._clock = pygame.time.Clock()
        pygame.display.set_caption("Space Invaders")

        #Create a surface
        self._space_surface = pygame.Surface((800,800))

        #Create spaceship
        self._space_ship = SpaceShip("assets/DurrrSpaceShip.png", 400, 800)

        #Create bullets
        self._all_bullets = pygame.sprite.Group()

    def run(self):
        #checks for events
        while True:
            #checks for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    current_ship_location = self._space_ship.get_position()
                    bullet_object = Bullet(current_ship_location[0] + 40, current_ship_location[1] + 10)
                    self._all_bullets.add(bullet_object)
                    print(self._all_bullets)
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                self._space_ship.move("d")
            if keys[pygame.K_a]:
                 self._space_ship.move("a")
            if keys[pygame.K_w]:
                 self._space_ship.move("w")
            if keys[pygame.K_s]:
                 self._space_ship.move("s")

            #places surface on window
            self._display.blit(self._space_surface, (0,0))
            self._space_surface.blit(pygame.image.load("assets/OuterSpace.png"), (0,0))
            self._space_surface.blit(self._space_ship.get_surface() , self._space_ship.get_position())
            self._all_bullets.draw(self._space_surface)
            self._all_bullets.update()

            #updates window
            pygame.display.update()
            self._clock.tick(60)

my_game = Game()
my_game.run()