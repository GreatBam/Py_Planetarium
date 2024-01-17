class Planet:
    def __init__(self, x: int, y: int, radius: int, color: tuple, screen: object, angle_increase: int, width: int, height: int):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen = screen
        self.angle_increase = angle_increase
        self.width = width
        self.height = height
        self.angle = 0