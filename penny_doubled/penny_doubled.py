import sys


def get_input():
    raw_input = input('Number of days: ')
    if not raw_input.isnumeric():
        print('You must enter a number')
        sys.exit(1)
    result = int(raw_input)
    if result <= 0:
        print('Please enter a positive number')
        sys.exit(1)
    return result


def main():
    num_days = get_input()
    result = .01 * (2 ** (num_days - 1))
    print('Doubling one penny for ' + str(num_days) + ' days -> ' + str(result))


if __name__ == '__main__':
    main()
