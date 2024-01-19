# Planetarium

# Imports
import pygame, random, math

# Functions
def shuffle(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest

# Classes
class Sun:
    def __init__(self, x: int, y: int, radius: int, color: tuple, screen: object):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen = screen
        
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

class Planet:
    def __init__(self, ratio_x: int, ratio_y: int, radius: int, color: tuple, screen: object, angle_increase: int):
        self.ratio_x = ratio_x
        self.ratio_y = ratio_y
        self.radius = radius
        self.color = color
        self.screen = screen
        self.angle_increase = angle_increase
        self.angle = 0
        
    def move(self):
        self.y = (int(math.cos(self.angle) * self.ratio_x) + WIDTH / 2)
        self.x = (int(math.sin(self.angle) * self.ratio_y) + HEIGHT / 2)
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        self.angle -= self.angle_increase
        
class Orbit:
    def __init__(self, x: int, y: int, color: tuple, screen: object):
        self.x = x
        self.y = y
        self.color = color
        self.screen = screen
        
    def draw(self):
        pygame.draw.ellipse(self.screen, self.color, (WIDTH/2-(self.x/2), HEIGHT/2-(self.y/2), self.x, self.y), 1)

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
sun = Sun((WIDTH/2),
          (HEIGHT/2),
          40,
          YELLOW,
          screen)

# Planets
venus = Planet (50,
                100,
                sizes_1[0],
                shuffled_colors[0],
                screen,
                shuffled_velocities[0])
mercury = Planet (100,
                150,
                sizes_1[1],
                shuffled_colors[1],
                screen,
                shuffled_velocities[1])
earth = Planet (150,
                200,
                sizes_1[2],
                shuffled_colors[2],
                screen,
                shuffled_velocities[2])
mars = Planet (200,
                250,
                shuffled_sizes[0],
                shuffled_colors[3],
                screen,
                shuffled_velocities[3])
jupiter = Planet (250,
                300,
                shuffled_sizes[1],
                shuffled_colors[4],
                screen,
                shuffled_velocities[4])
saturn = Planet (300,
                350,
                shuffled_sizes[2],
                shuffled_colors[5],
                screen,
                shuffled_velocities[5])
uranus = Planet (350,
                400,
                shuffled_sizes[3],
                shuffled_colors[6],
                screen,
                shuffled_velocities[6])
neptune = Planet (400,
                450,
                shuffled_sizes[4],
                shuffled_colors[7],
                screen,
                shuffled_velocities[7])

# Orbits
venus_orbit = Orbit(200,
                    100,
                    shuffled_colors[0],
                    screen)
mercury_orbit = Orbit(300,
                    200,
                    shuffled_colors[1],
                    screen)
earth_orbit = Orbit(400,
                    300,
                    shuffled_colors[2],
                    screen)
mars_orbit = Orbit(500,
                    400,
                    shuffled_colors[3],
                    screen)
jupiter_orbit = Orbit(600,
                    500,
                    shuffled_colors[4],
                    screen)
saturn_orbit = Orbit(700,
                    600,
                    shuffled_colors[5],
                    screen)
uranus_orbit = Orbit(800,
                    700,
                    shuffled_colors[6],
                    screen)
neptune_orbit = Orbit(900,
                    800,
                    shuffled_colors[7],
                    screen)

# Objects list
planets = [venus, mercury, earth, mars, jupiter, saturn, uranus, neptune]
orbits = [venus_orbit, mercury_orbit, earth_orbit, mars_orbit, jupiter_orbit, saturn_orbit, uranus_orbit, neptune_orbit]

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
    for orbit in orbits:
        orbit.draw()
    
    # Planets
    for planet in planets:
        planet.move()
    
    # Draw
    pygame.display.flip()
    clock.tick(60)
    
# Close window on quit
pygame.quit()