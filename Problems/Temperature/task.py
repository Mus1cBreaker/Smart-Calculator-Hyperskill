def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 2)


def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


def main():
    fahrenheit = "F"
    celsius = "C"
    temperature, unit = input().split()  # read the input
    if unit == fahrenheit:
        print(str(fahrenheit_to_celsius(float(temperature))) + " C")
    if unit == celsius:
        print(str(celsius_to_fahrenheit(float(temperature))) + " F")
