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


def show_transactions(n):
    balance = .01
    for i in range(n):
        print('Day', i + 1, 'balance:', balance)
        balance *= 2


def main():
    num_days = get_input()
    print('Daily Transactions')
    print('------------------')
    show_transactions(num_days)
    print('------------------')
    result = .01 * (2 ** (num_days - 1))
    print('Doubling one penny for', num_days, 'days ->', result)


if __name__ == '__main__':
    main()
