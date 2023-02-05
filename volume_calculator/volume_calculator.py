import math
import re
import sys


# Area of a sphere is 4 * pi * radius^2
def calc_area(radius):
    return 4 * math.pi * radius ** 2


# Volume of a sphere is 4/3 * pi * radius^3
def calc_volume(radius):
    return 4/3 * math.pi * radius ** 3


def get_input():
    user_input = input('Enter the radius: ')
    data = re.findall(r'(\d+)([^.\d]*)', user_input)
    if len(data) < 1:
        print('ERROR: You must enter an integer value for radius')
        sys.exit(1)
    radius, units = data[0]
    radius = int(radius)
    if len(units) > 0:
        units = units.strip()
    return radius, units


def get_units(units, exp):
    return units+'^'+str(exp) if len(units) > 0 else ''


def main():
    radius, units = get_input()
    print('Volume:', calc_volume(radius), get_units(units, 3))
    print('Area:', calc_area(radius), get_units(units, 2))


if __name__ == '__main__':
    main()
