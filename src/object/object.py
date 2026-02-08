from settings import *

from object.rooted_object import RootedObject

class Object(RootedObject):
    def __init__(self, position: Vector2, mass: int,  radius: int, color: Color):
        super().__init__(position, mass, radius, color)

        self.velocity: Vector2 = vector2_zero()
        self.acceleration: Vector2 = vector2_zero()
    
    def calculate_velocity(self, others):
        F_net = vector2_zero()
        for other in others:
            if other is not self:
                d2 = vector2_distance_sqr(self.position, other.position)
                theta = -vector2_line_angle(self.position, other.position)

                try:
                    F_obj = Vector2((self.mass * other.mass) / d2, 0)
                except ZeroDivisionError:
                    F_obj = vector2_zero()
                
                F_obj = vector2_rotate(F_obj, theta)
                F_net = vector2_add(F_net, F_obj)

        self.acceleration = vector2_scale(F_net, 1 / self.mass)
        self.velocity = vector2_scale(vector2_add(self.velocity, self.acceleration), 1)
        self.velocity = vector2_clamp_value(self.velocity, 0, 25) # clamp velocity so that objects don't fly off at mach 50

    def update(self):
        self.position = vector2_add(self.position, self.velocity)

        # keep objects contained within screen
        if self.position.x < -self.radius / 2:
            self.position.x = SCREEN_WIDTH + self.radius / 2
        elif self.position.x > SCREEN_WIDTH + self.radius / 2:
            self.position.x = -self.radius / 2
        
        if self.position.y < -self.radius / 2:
            self.position.y = SCREEN_HEIGHT + self.radius / 2
        elif self.position.y > SCREEN_HEIGHT + self.radius / 2:
            self.position.y = -self.radius / 2
    
    def draw(self, debug: bool):
        super().draw(debug)
        
        if debug:
            draw_line_v(self.position, vector2_add(self.position, vector2_scale(self.velocity, 100)), MAROON)
            velocity_end = vector2_add(self.position, vector2_scale(self.velocity, 100))
            draw_line_v(velocity_end, vector2_add(velocity_end, vector2_scale(self.acceleration, 500)), PINK)
