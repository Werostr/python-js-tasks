import math

vector2D = [1, 1]
list2D = [(1, 1), (2, 1), (2, 2, 2), (3, 3), (-1, -1)]
vector3D = [1, 1, 1]
list3D = [(1, 1, 1), (2, 1, 2), (2, 2, 2), (3, 3, 3), (-1, -1, -1)]
radius = 2


def distance2D(vector, radius, list):
    ok_list = []
    for point in list:
        if (
            math.sqrt((vector[0] - point[0]) ** 2 + (vector[1] - point[1]) ** 2)
            < radius
        ):
            ok_list.append(point)
    return ok_list


# print(distance2D(vector2D,radius,list2D))


def distance3D(vector, radius, list):
    ok_list = []
    for point in list:
        if (
            math.sqrt(
                (vector[0] - point[0]) ** 2
                + (vector[1] - point[1]) ** 2
                + (vector[2] - point[2]) ** 2
            )
            < radius
        ):
            ok_list.append(point)
    return ok_list


print(distance3D(vector3D, radius, list3D))


circle1 = [2, 2]
circle2 = [3, 1]
radius1 = 2
radius2 = 3


def twoCircles(circle1, circle2, radius1, radius2):
    if (
        math.sqrt((circle1[0] - circle2[0]) ** 2 + (circle1[1] - circle2[1]) ** 2)
        < radius1 + radius2
    ):
        return 1
    return 0


print(twoCircles(circle1, circle2, radius1, radius2))
