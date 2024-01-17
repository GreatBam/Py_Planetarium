import pygame

class Sun:
    def __init__(self, x: int, y: int, radius: int, color: tuple, screen: object):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen = screen
        
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)