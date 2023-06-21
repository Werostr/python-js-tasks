import math


class Circle:
    def __init__(self):
        self.position = (0, 0)
        self.radius = 0

    def __init__(self, positon, radius):
        self.position = positon
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius

    def teleport(self, new_position):
        self.position = new_position

    def move(self, vector):
        self.position = (self.position[0] + vector[0], self.position[1] + vector[1])


class World:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.players = []

    def get_player(self, player_id):
        return self.players[player_id]

    def move_player():
        pass


def colision(circle1, circle2):
    if (
        math.sqrt(
            (circle1.position[0] - circle2.position[0]) ** 2
            + (circle1.position[1] - circle2.position[1]) ** 2
        )
        < circle1.radius + circle2.radius
    ):
        return True
    return False


k1 = Circle((1, 1), 2)
k2 = Circle((0, 0), 1)

print(colision(k1, k2))
