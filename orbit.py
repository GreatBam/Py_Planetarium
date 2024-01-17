import pygame

class Orbit:
    def __init__(self, x, y, color, screen):
        self.x = x
        self.y = y
        self.color = color
        self.screen = screen
        
    def draw(self):
        pygame.draw.ellipse(self.screen, self.color, (400-(self.x/2), 400-(self.y/2), self.x, self.y), 1)