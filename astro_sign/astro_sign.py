from datetime import date
import json
import re


class AstrologicalSign:
    def __init__(self, name, from_date, to_date, traits):
        self.name = name
        self.from_date = from_date
        self.to_date = to_date
        self.traits = traits


def read_input(filename):
    with open(filename) as file:
        return json.load(file)


def parse_data(data):
    result = {}
    this_year = date.today().year
    for key in data:
        m1 = data[key][0]
        d1 = data[key][1]
        from_date = date(this_year, m1, d1)
        m2 = data[key][2]
        d2 = data[key][3]
        to_date = date(this_year, m2, d2)
        t = data[key][4]
        result[key] = AstrologicalSign(key, from_date, to_date, t)
    return result


def find_sign(input_date, signs):
    for key in signs:
        if signs[key].from_date <= input_date <= signs[key].to_date:
            return signs[key]
    return None


def main():
    raw_data = read_input('astro_data.json')
    signs = parse_data(raw_data)
    input_re = re.compile(r'^(\d+)/(\d+)$')
    this_year = date.today().year
    while True:
        birthday = input('Enter your birthday (mm/dd): ')
        m = re.match(input_re, birthday)
        if m is None:
            print('Invalid input')
            break
        birth_date = date(this_year, int(m.group(1)), int(m.group(2)))
        sign = find_sign(birth_date, signs)
        if sign is None:
            print('Error finding your sign')
            break
        print('Your sign is:', sign.name)
        print('Your traits are:', sign.traits)


if __name__ == '__main__':
    main()
