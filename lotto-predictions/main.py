from typing import Set, Dict
from random import randint
from math import isinf


def money_to_invest_per_week() -> float:
    while True:
        try:
            money = float(input("Enter how much money do you want to invest per week: "))
            if isinf(money):
                print("You cannot invest infinity!\n")
            elif money <= 0:
                print("You cannot invest negative or equals to zero numbers!\n")
            else:
                return money

        except ValueError:
            print("Only numbers can be entered!\n")


def currency_of_money() -> str:
    while True:
        currency = input("Enter the currency in which you want to invest (You can choose: EUR, USD or PLN): ")
        if currency.upper() in ("EUR", "USD", "PLN"):
            return currency
        else:
            print("You can choose only between EUR, USD or PLN\n")


def frequency_of_draws_per_week() -> int:
    while True:
        frequency = input("Enter how many times a week do you want to draw (you can only 1 to 3 times): ")
        if frequency in ("1", "2", "3"):
            return int(frequency)
        else:
            print("You can choose only 1, 2 or 3\n")


def enter_player_numbers() -> Set[int]:
    player_numbers = set()
    number_ending = {1: "st", 2: "nd", 3: "rd"}

    while len(player_numbers) < AMOUNT_OF_NUMBERS_IN_LOTTO:
        try:
            which_number_is_entered = len(player_numbers) + 1
            entered_number = int(input(
                f"Enter the {which_number_is_entered}"
                f"{number_ending[which_number_is_entered] if which_number_is_entered in number_ending else 'th'} "
                f"number: "
            ))
            if MIN_NUMBER_IN_LOTTO <= entered_number <= MAX_NUMBER_IN_LOTTO:

                if entered_number not in player_numbers:
                    player_numbers.add(entered_number)
                else:
                    print(
                        "You can't give the same number several times!\n"
                        "Please enter a different number!\n"
                    )

            else:
                print(
                    "You entered a number outside the range\n"
                    "Enter a new number between 1 and 49!\n"
                )

        except ValueError:
            print("You can only enter natural numbers\n")

    return player_numbers


def draw_win_numbers() -> Set[int]:
    win_numbers = set()
    while len(win_numbers) < AMOUNT_OF_NUMBERS_IN_LOTTO:
        win_numbers.add(randint(MIN_NUMBER_IN_LOTTO, MAX_NUMBER_IN_LOTTO))

    return win_numbers


class Simulation:
    def __init__(self, player_numbers: Set[int]) -> None:
        self.player_numbers = player_numbers
        self.weeks = 0
        self.hit_specific_numbers = {
            "three": 0,
            "four": 0,
            "five": 0,
        }

    def hit_numbers(self) -> Dict[str, int]:
        win_numbers = draw_win_numbers()

        print(f"\nYour numbers: {', '.join(map(str, self.player_numbers))}")
        print("Calculations...\n")

        while self.player_numbers != win_numbers:
            counter = 0

            for player_number in self.player_numbers:
                if player_number in win_numbers:
                    counter += 1

            if counter == 3:
                self.hit_specific_numbers["three"] += 1
            elif counter == 4:
                self.hit_specific_numbers["four"] += 1
            elif counter == 5:
                self.hit_specific_numbers["five"] += 1

            self.weeks += 1
            win_numbers = draw_win_numbers()

        return self.hit_specific_numbers

    def spent_time(self, draws_per_week: int) -> Dict[str, int]:
        days = self.weeks * 7 // draws_per_week
        spent_years = (days // 365)

        if days >= 365:
            spent_days = days - spent_years * 365
        else:
            spent_days = days

        return {
            "years": spent_years,
            "days": spent_days
        }


def main() -> None:
    print(
        "WELCOME TO THE LOTTO PREDICTIONS. "
        "WE WILL SIMULATE HITTING A SIX IN THE LOTTO.\n"
        "REMEMBER! YOU CAN ONLY SELECT NUMBERS BETWEEN 1 AND 49, BUT THEY CAN'T REPEAT.\n"
    )

    spent_money_per_week = money_to_invest_per_week()
    type_of_currency = currency_of_money()
    draws_per_week = frequency_of_draws_per_week()

    app = Simulation(enter_player_numbers())
    hit_numbers = app.hit_numbers()
    spent_time = app.spent_time(draws_per_week)

    print(
        f"The six fell out after {spent_time['years']} year{'s' if spent_time['years'] > 1 else ''} and "
        f"{spent_time['days']} day{'s' if spent_time['days'] > 1 else ''}"
    )
    print(f"You spent {app.weeks * spent_money_per_week} {type_of_currency}\n")
    print(
        f"During the draw:\n"
        f"three was drawn {hit_numbers['three']} time{'s' if hit_numbers['three'] > 1 else ''}\n"
        f"four was drawn {hit_numbers['four']} time{'s' if hit_numbers['four'] > 1 else ''}\n"
        f"five was drawn {hit_numbers['five']} time{'s' if hit_numbers['five'] > 1 else ''}"
    )


if __name__ == '__main__':
    MIN_NUMBER_IN_LOTTO = 1
    MAX_NUMBER_IN_LOTTO = 49
    AMOUNT_OF_NUMBERS_IN_LOTTO = 6

    main()
