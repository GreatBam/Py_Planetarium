import pygame

class Orbit:
    def __init__(self, x: int, y: int, color: tuple, screen: object, width: int, height: int):
        self.x = x
        self.y = y
        self.color = color
        self.screen = screen
        self.width = width
        self.height = height
        
    def draw(self):
        pygame.draw.ellipse(self.screen, self.color, (self.width/2-(self.x/2), self.height/2-(self.y/2), self.x, self.y), 1)