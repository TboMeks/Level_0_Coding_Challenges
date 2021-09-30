def is_triangle(a, b, c):
    if (a + b > c) or (a + c > c) or (b + c > b):
        print("No")
    else:
        print("Yes")
