import os
import sys


class ProductQuantity:
    def __init__(self, product_name: str) -> None:
        self.product_name = product_name
        self._product_quantity = 0

    @property
    def quantity(self) -> int:
        return self._product_quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        if value < 0:
            print('\nProduct quantity must be positive')
        else:
            self._product_quantity = value


def create_updated_data() -> None:
    with open('products.txt', 'r') as products_data:
        if products_data.readable():
            data = products_data.readlines()
            for line in data:
                if line.split(':')[1] == searched_product.product_name:
                    searched_product.quantity = int(line.split(':')[2])
                    helper = searched_product.quantity
                    choose_action()

                    if helper != searched_product.quantity:
                        data[data.index(line)] = line.replace(line.split(':')[2], str(searched_product.quantity)) + '\n'
                        save_updated_data(data)
                    return

            print("\nWe don't have this product")

        else:
            raise "Error with file"


def choose_action() -> None:
    while True:
        choice = input('\nChoose the option:\n'
                       '1. Add any number of product\n'
                       '2. Delete any number of product\n'
                       '3. Change product quantity\n'
                       '4. Back to main menu\n')

        if choice == '4':
            print('')
            break

        if choice not in ('1', '2', '3'):
            print("\nWe don't have that option")
            continue

        while True:
            try:
                quantity_to_change = input(f'\nIf you want come back write Back\n'
                                           f'Write how much would you like to {options[int(choice)]}: ')
                if quantity_to_change.capitalize() == 'Back':
                    quantity_to_change = 'Back'
                    break
                quantity_to_change = int(quantity_to_change)

            except ValueError:
                print('\nYou can only enter a number')

            else:
                if choice == '1':
                    searched_product.quantity += quantity_to_change
                elif choice == '2':
                    searched_product.quantity -= quantity_to_change
                else:
                    searched_product.quantity = quantity_to_change
                break

        if quantity_to_change != 'Back':
            break

options = {
    1: 'add',
    2: 'subtract',
    3: 'change'
}


def save_updated_data(data_to_save: list[str]) -> None:
    with open('products.txt', 'w') as write_the_products:
        if write_the_products.writable():
            write_the_products.writelines(data_to_save)
            print('\nSuccess')
        else:
            raise "Error with file"


def main() -> None:
    if os.stat('products.txt').st_size == 0:
        raise 'Database is empty'

    create_updated_data()


def add_product():
    name = input('Enter name of your product: ')
    while True:
        try:
            quantity = int(input('Enter quantity of your product: '))
            break
        except ValueError:
            print('\nYou can only enter a number, try again')

    with open('products.txt', 'r+') as products:
        product_id = len(products.readlines()) + 1

        products.write(f'{product_id}:{name.capitalize()}:{quantity}\n')
        print('\nSuccessful added\n')


if __name__ == "__main__":
    while True:
        action = input('If you want add the product write -> Add\n'
                       'If you want choose any product write -> Product\n'
                       'If you want exit the program write -> Exit\n')

        if action.capitalize() == 'Add':
            add_product()

        elif action.capitalize() == 'Exit':
            print('\nSuccessful exit from the program')
            sys.exit()

        elif action.capitalize() == 'Product':
            searched_product = ProductQuantity(str(input(
                "\nEnter your chosen product or if you want back to main menu write -> Back: ")).capitalize())
            if searched_product == 'Back':
                continue
            main()

        else:
            print('\nWrong data, try again')
