# -*- coding: utf-8 -*-


def is_valid(func):

    def wrapper(self, other):
        if len(self.coordinates) == len(other.coordinates):
            return func(self, other)
        else:
            raise TypeError("Unsupported operands error - Vectors must be the same dimension")

    return wrapper


class Vector:
    def __init__(self, *args):
        self.coordinates = list(args)

    @is_valid
    def __add__(self, other):
        new_vector = []
        for i in zip(self.coordinates, other.coordinates):
            new_vector.append(sum(i))
        return new_vector

    @is_valid
    def __sub__(self, other):
        new_vector = []
        for i in zip(self.coordinates, other.coordinates):
            new_vector.append(i[0] - i[1])
        return new_vector

    @is_valid
    def __matmul__(self, other):
        scalar = 0
        for i in zip(self.coordinates, other.coordinates):
            scalar += i[0] * i[1]
        return scalar

    @is_valid
    def __mul__(self, other):
        new_vector = []

        if isinstance(other, int):
            for i in self.coordinates:
                new_vector.append(i * other)
        else:
            f_vector = self.coordinates
            s_vector = other.coordinates
            if len(f_vector) == 3:
                new_vector = [
                    f_vector[1] * s_vector[2] - f_vector[2] * s_vector[1],
                    f_vector[0] * s_vector[2] - f_vector[2] * s_vector[0],
                    f_vector[0] * s_vector[1] - f_vector[1] * s_vector[0]
                              ]
            else:
                return "Vectors must be three-dimensional"
        return new_vector


if __name__ == '__main__':
    vector1 = Vector(1, 2, 3)
    vector2 = Vector(4, 5, 6)
    vector3 = vector1 @ vector2
    vector4 = vector1 * vector2
    print(vector4)
