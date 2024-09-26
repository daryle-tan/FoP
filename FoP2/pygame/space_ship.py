import pygame

class SpaceShip:

    def __init__(self, image, x, y):
        self._space_ship_surface = pygame.image.load(image)
        self.rect = self._space_ship_surface.get_rect(midbottom=(x,y))

    def get_position(self):
        return (self.rect.x, self.rect.y)
    
    def get_surface(self):
        return self._space_ship_surface
    
    def move(self, direction):
        if direction == "a":
            if self.rect.x >= 20:
                self.rect.x -= 5
        elif direction == "d":
            if self.rect.x <= 700:
                self.rect.x += 5
        elif direction == "w":
            if self.rect.y >=  300:
                self.rect.y -= 5
        elif direction == "s":
            if self.rect.y <= 700:
                self.rect.y += 5