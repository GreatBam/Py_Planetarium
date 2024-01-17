# Planetarium

# Imports
import pygame, random
from sun import Sun
from planet import Planet
from orbit import Orbit

def shuffle(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest

# Constants
WIDTH = 850
HEIGHT = 850

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# lists for random sizes, colors and velocities
sizes_1 = [8, 10, 15]
sizes_2 = [20, 25, 30, 35, 36]
shuffled_sizes = shuffle(sizes_2)
colors = [RED, GREEN, BLUE, PURPLE, ORANGE, WHITE, GREY, YELLOW]
shuffled_colors = shuffle(colors)
velocities = [0.01, 0.005, 0.003, 0.002, 0.001, 0.0005, 0.0003, 0.0001]
shuffled_velocities = shuffle(velocities)

# Pygame setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planetarium")
rand = random.randint(0, 7)
running = True

# Sun
sun = Sun(WIDTH/2, HEIGHT/2, 40, YELLOW, screen)

# Planets
venus = Planet (50, 100, sizes_1[0], shuffled_colors[0], screen, shuffled_velocities[0], WIDTH, HEIGHT)
mercury = Planet (100, 150, sizes_1[1], shuffled_colors[1], screen, shuffled_velocities[1], WIDTH, HEIGHT)
earth = Planet (150, 200, sizes_1[2], shuffled_colors[2], screen, shuffled_velocities[2], WIDTH, HEIGHT)
mars = Planet (200, 250, shuffled_sizes[0], shuffled_colors[3], screen, shuffled_velocities[3], WIDTH, HEIGHT)
jupiter = Planet (250, 300, shuffled_sizes[1], shuffled_colors[4], screen, shuffled_velocities[4], WIDTH, HEIGHT)
saturn = Planet (300, 350, shuffled_sizes[2], shuffled_colors[5], screen, shuffled_velocities[5], WIDTH, HEIGHT)
uranus = Planet (350, 400, shuffled_sizes[3], shuffled_colors[6], screen, shuffled_velocities[6], WIDTH, HEIGHT)
neptune = Planet (400, 450, shuffled_sizes[4], shuffled_colors[7], screen, shuffled_velocities[7], WIDTH, HEIGHT)

# Orbits
venus_orbit = Orbit(200, 100, shuffled_colors[0], screen, WIDTH, HEIGHT)
mercury_orbit = Orbit(300, 200, shuffled_colors[1], screen, WIDTH, HEIGHT)
earth_orbit = Orbit(400, 300, shuffled_colors[2], screen, WIDTH, HEIGHT)
mars_orbit = Orbit(500, 400, shuffled_colors[3], screen, WIDTH, HEIGHT)
jupiter_orbit = Orbit(600, 500, shuffled_colors[4], screen, WIDTH, HEIGHT)
saturn_orbit = Orbit(700, 600, shuffled_colors[5], screen, WIDTH, HEIGHT)
uranus_orbit = Orbit(800, 700, shuffled_colors[6], screen, WIDTH, HEIGHT)
neptune_orbit = Orbit(900, 800, shuffled_colors[7], screen, WIDTH, HEIGHT)

# Main loop
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Logic
    screen.fill(BLACK)
    sun.draw()
    
    # Orbits
    venus_orbit.draw()
    mercury_orbit.draw()
    earth_orbit.draw()
    mars_orbit.draw()
    jupiter_orbit.draw()
    saturn_orbit.draw()
    # uranus_orbit.draw()
    # neptune_orbit.draw()
    
    # Planets
    venus.move()
    mercury.move()
    earth.move()
    mars.move()
    jupiter.move()
    saturn.move()
    # uranus.move()
    # neptune.move()
    
    # Draw
    pygame.display.flip()
    clock.tick(60)
    
# Close window on quit
pygame.quit()