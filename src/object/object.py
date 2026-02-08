from settings import *

class Object:
    def __init__(self, position: Vector2, mass: int,  radius: int, color: Color):
        self.position = position
        self.mass = mass
        self.radius = radius
        self.color = color

        self.velocity: Vector2 = vector2_zero()
        self.acceleration: Vector2 = vector2_zero()
    
    def calculate_velocity(self, others):
        F_net = vector2_zero()
        for other in others:
            if other is not self:
                dist = vector2_distance(self.position, other.position) * SCALE_FACTOR
                theta = -vector2_line_angle(self.position, other.position)

                try:
                    F_obj = Vector2((self.mass * other.mass) / (dist ** 2), 0)
                except ZeroDivisionError:
                    F_obj = vector2_zero()
                
                F_obj = vector2_rotate(F_obj, theta)
                F_net = vector2_add(F_net, F_obj)

        self.acceleration = vector2_scale(F_net, 1 / self.mass)
        self.velocity = vector2_scale(vector2_add(self.velocity, self.acceleration), 1)
        self.velocity = vector2_clamp_value(self.velocity, 0, 25) # clamp velocity so that objects don't fly off at mach 50

    def update(self):
        self.position = vector2_add(self.position, self.velocity)
    
    def draw(self, debug: bool):
        draw_circle_v(self.position, self.radius, self.color)
        
        if debug:
            draw_line_v(self.position, vector2_add(self.position, vector2_scale(self.velocity, 100)), MAROON)
            velocity_end = vector2_add(self.position, vector2_scale(self.velocity, 100))
            draw_line_v(velocity_end, vector2_add(velocity_end, vector2_scale(self.acceleration, 500)), PINK)
