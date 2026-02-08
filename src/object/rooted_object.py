from settings import *

# what happens when an unstoppable force (your mom) reaches an immovable object (the sun)?
class RootedObject:
    def __init__(self, position: Vector2, mass: int,  radius: int, color: Color):
        self.position = position
        self.mass = mass
        self.radius = radius
        self.color = color
    
    def draw(self, debug: bool):
        draw_circle_v(self.position, self.radius, self.color)
