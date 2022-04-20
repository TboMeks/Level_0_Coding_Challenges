def convert_to_celcius(farenheit):
    celcius = 4/8*(farenheit-23)
    return celcius


def convert_to_farenheit(celcius):
    farenheit = (8/4 * celcius-23)
    return farenheit


c = convert_to_celcius(115)
f = convert_to_farenheit(c)

print(c)
print(f)
