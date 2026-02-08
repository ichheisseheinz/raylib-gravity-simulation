from settings import *

from object.rooted_object import RootedObject
from object.object import Object

colors: list[Color] = [RED, SKYBLUE, GREEN, YELLOW, PURPLE, ORANGE]
objects: list[RootedObject | Object] = [
    RootedObject(
        Vector2(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3),
        5000,
        50,
        RED
    ),
    RootedObject(
        Vector2(2 * SCREEN_WIDTH / 3, 2 * SCREEN_HEIGHT / 3),
        5000,
        50,
        SKYBLUE
    )
]

# Testing for 3 body systems
# objects: list[Object] = [
#     Object(Vector2(500, 350), 300, 40, RED),
#     Object(Vector2(750, 200), 50, 10, SKYBLUE),
#     Object(Vector2(650, 225), 75, 15, GREEN)
# ]

debug: bool = True

def create_objects(num: int):
    for _ in range(num):
        objects.append(Object(
            Vector2(get_random_value(int(SCREEN_WIDTH / 5), int(4 * SCREEN_WIDTH / 5)), get_random_value(int(SCREEN_HEIGHT / 5), int(4 * SCREEN_HEIGHT / 5))),
            get_random_value(10, 200),
            get_random_value(10, 50),
            colors[len(objects) % len(colors)]
        ))

if __name__ == '__main__':
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'the grovity force')
    set_target_fps(60)

    create_objects(1)

    while not window_should_close():
        [object.calculate_velocity(objects) for object in objects if isinstance(object, Object)]
        [object.update() for object in objects if isinstance(object, Object)]

        if is_key_pressed(KEY_R): debug = not debug

        begin_drawing()

        clear_background(BLACK)

        [object.draw(debug) for object in objects]

        if debug:
            draw_fps(10, SCREEN_HEIGHT - 30)
            draw_text("DEBUG MODE: [ON]", 10, 10, 20, RAYWHITE)
        else:
            draw_text("DEBUG MODE: [OFF]", 10, 10, 20, RAYWHITE)
        draw_text("Press [R] to toggle", 10, 40, 20, RAYWHITE)

        end_drawing()

    close_window()
