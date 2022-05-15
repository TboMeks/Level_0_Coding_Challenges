def area_of_a_triangle(a, b, c):
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c))**0.5

    return area


area_of_a_triangle(3, 4, 5)
