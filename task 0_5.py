def area_of_a_triangle(side1, side2, side3):
    area_of_a_triangle = (side1 + side2 + side3) / 2
    area = (s*(s-side1)*(s-side2)*(s-side3))**0.5

    return area


area_of_a_triangle(3, 4, 5)
