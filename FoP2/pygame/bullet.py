import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255,0,0,255), (5,5), 5)
        self.rect = self.image.get_rect(midbottom=(x,y))

    def update(self):
        self.rect.y -= 20