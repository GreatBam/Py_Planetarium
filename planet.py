# import pygame, sys, math

# class Planet:
#     def __init__(self, ratio_x: int, ratio_y: int, radius: int, color: tuple, screen: object, angle_increase: int):
#         self.ratio_x = ratio_x
#         self.ratio_y = ratio_y
#         self.radius = radius
#         self.color = color
#         self.screen = screen
#         self.angle_increase = angle_increase
#         self.angle = 0
#         # self.x = WIDTH / 2
#         # self.y = HEIGHT / 2
        
#     def move(self):
#         self.y = (int(math.cos(self.angle) * self.ratio_x) + WIDTH / 2)
#         self.x = (int(math.sin(self.angle) * self.ratio_y) + HEIGHT / 2)
#         pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
#         self.angle -= self.angle_increase