# Planetarium

# Imports
import pygame
from sun import Sun
from planet import Planet
from orbit import Orbit

# Constants
WIDTH = 800
HEIGHT = 800

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Pygame setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planetarium")
running = True

# Planets
sun = Sun(40, YELLOW, screen)
venus = Planet (50, 100, 10, GREY, screen, 0.01, WIDTH, HEIGHT)
mercury = Planet (100, 150, 15, ORANGE, screen, 0.005, WIDTH, HEIGHT)
earth = Planet (150, 200, 20, BLUE, screen, 0.003, WIDTH, HEIGHT)
mars = Planet (200, 250, 25, RED, screen, 0.002, WIDTH, HEIGHT)
jupiter = Planet (250, 300, 30, PURPLE, screen, 0.001, WIDTH, HEIGHT)
saturn = Planet (300, 350, 35, GREEN, screen, 0.0005, WIDTH, HEIGHT)
uranus = Planet (350, 400, 40, WHITE, screen, 0.0003, WIDTH, HEIGHT)
neptune = Planet (400, 450, 45, GREY, screen, 0.0001, WIDTH, HEIGHT)

# Orbits
venus_orbit = Orbit(200, 100, WHITE, screen)
mercury_orbit = Orbit(300, 200, WHITE, screen)
earth_orbit = Orbit(400, 300, WHITE, screen)
mars_orbit = Orbit(500, 400, WHITE, screen)
jupiter_orbit = Orbit(600, 500, WHITE, screen)
saturn_orbit = Orbit(700, 600, WHITE, screen)
uranus_orbit = Orbit(800, 700, WHITE, screen)
neptune_orbit = Orbit(900, 800, WHITE, screen)

# Main loop
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Logic
    screen.fill(BLACK)
    sun.draw()
    venus_orbit.draw()
    mercury_orbit.draw()
    earth_orbit.draw()
    mars_orbit.draw()
    jupiter_orbit.draw()
    saturn_orbit.draw()
    uranus_orbit.draw()
    neptune_orbit.draw()
    venus.move()
    mercury.move()
    earth.move()
    mars.move()
    jupiter.move()
    saturn.move()
    uranus.move()
    neptune.move()
    
    # Draw
    pygame.display.flip()
    clock.tick(60)
    
# Close window on quit
pygame.quit()