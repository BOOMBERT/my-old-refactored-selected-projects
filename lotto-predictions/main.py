from random import randint
from math import isinf

print('WELCOME TO THE SIMULATOR OF HITTING SIXES IN THE LOTTO')
print("REMEMBER! YOU CAN ONLY SELECT NUMBERS BETWEEN 1 AND 49, BUT THEY CAN'T REPEAT\n")

def how_much_money():
    while True:
        try:
            invested_money = float(input('Enter how much money do you want to invest per week: '))
            if isinf(invested_money):
                print('You cannot give infinity!')
            else:
                return invested_money
        except ValueError:
            print('Only numbers can be entered!')

def currency_of_money():
    while True:
        currency = str(input('Enter the currency in which you want to pay (You can choose: EUR, USD or PLN): '))
        if currency.upper() in ('EUR', 'USD', 'PLN'):
            return currency
        else:
            print('You can choose only between EUR, USD or PLN')

def how_often_to_draws():
    while True:
        how_often = int(input('Enter how many times a week do you want to draw (you can only 1 to 3 times): '))
        if how_often in (1, 2, 3):
            return how_often
        else:
            print('You can choose only 1, 2 or 3')

def entering_player_numbers():
    player_numbers = set()
    while len(player_numbers) < 6:
        try:
            entered_number = int(input(f'Enter the {len(player_numbers)+1} number: '))
            if 1 <= entered_number <= 49:
                if entered_number not in player_numbers:
                    player_numbers.add(entered_number)
                else:
                    print("You can't give the same number several times!")
                    print('Please enter a different number!')
            else:
                print('You entered a number outside the range')
                print('Enter a new number between 1 and 49!')
        except ValueError:
            print('You can only enter natural numbers')

    return player_numbers

def drawing_of_winning_numbers():
    winning_numbers = set()
    while len(winning_numbers) < 6:
        winning_numbers.add(randint(1, 49))

    return winning_numbers

def main(spent_money_per_week, type_of_currency, frequency_of_draws, player_numbers):
    random_six_numbers = drawing_of_winning_numbers()
    print(f'Your numbers: {sorted(player_numbers)}\n')
    print('Calculations...\n')

    drawn_three = drawn_four = drawn_five = weeks = 0
    while player_numbers != random_six_numbers:
        counter = 0
        for i in player_numbers:
            if i in random_six_numbers:
                counter += 1

        if counter == 3:
            drawn_three += 1
        elif counter == 4:
            drawn_four += 1
        elif counter == 5:
            drawn_five += 1

        weeks += 1
        random_six_numbers = drawing_of_winning_numbers()

    days = weeks * 7 / frequency_of_draws
    years = (int(days / 365))

    if days >= 365:
        how_many_days = (days - years * 365)
    else:
        how_many_days = days

    print(f'The six fell out after {years} years and {int(how_many_days)} days')
    print(f'You spent {weeks * spent_money_per_week} {type_of_currency}')
    print(f'During the draw:\n'
          f'three were drawn {drawn_three} times\n'
          f'four were drawn {drawn_four} times\n'
          f'five were drawn {drawn_five} times')

if __name__ == '__main__':
    main(how_much_money(), currency_of_money(), how_often_to_draws(), entering_player_numbers())
