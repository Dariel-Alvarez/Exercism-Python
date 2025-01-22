def equilateral(sides):

    return sides[0] == sides[1] and sides[1] == sides[2] and is_triangle(sides)


def isosceles(sides):
    a, b, c = sides
    return (a == b or a == c or b == c) and is_triangle(sides)


def scalene(sides):
    a, b, c = sides
    return a != b and a != c and b != c and is_triangle(sides)


def is_triangle(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    return a + b >= c and b + c >= a and a + c >= b
