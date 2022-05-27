def max(*numbers):
    max = numbers[0]
    for i in numbers:
        if i >= max:
            max = i

    return max


print(max(1, 2, 3))
