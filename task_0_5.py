def area_of_a_triangle(side1, side2, side3):
    semiperimeter = (side1 + side2 + side3) / 2
    area_of_a_triangle = (semiperimeter*(semiperimeter-side1)
                          * (semiperimeter-side2) * (semiperimeter-side3)) ** 0.5

    return area_of_a_triangle


print(area_of_a_triangle(3, 4, 5))
