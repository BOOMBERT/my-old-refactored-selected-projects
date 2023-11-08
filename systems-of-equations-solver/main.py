from typing import List, Tuple
from math import isfinite


def get_space_separated_numbers_from_text(user_input: str, expected_amount_of_numbers: int) -> List[float] | ValueError:
    separated_user_numbers = user_input.split()
    if len(separated_user_numbers) != expected_amount_of_numbers:
        raise ValueError("Entered incorrect amount of elements")

    user_numbers = []

    for number in separated_user_numbers:
        try:
            number = float(number)
            user_numbers.append(number)
        except ValueError:
            raise ValueError("Entered wrong data")

        if not isfinite(number):
            raise ValueError("Entered infinity")

    return user_numbers


def addition_or_subtraction_sign(number: float) -> str:
    return "-" if number < 0 else "+"


def calculating_system_of_equations_with_two_unknowns() -> Tuple[float, float] | bool:
    AMOUNT_OF_NUMBERS_IN_ONE_EXPRESSION = 3

    a1x, b1y, c1 = get_space_separated_numbers_from_text(
        input("Enter a1x b1y c1 sequentially after the spaces: "), AMOUNT_OF_NUMBERS_IN_ONE_EXPRESSION
    )
    a2x, b2y, c2 = get_space_separated_numbers_from_text(
        input("Enter a2x b2y c2 sequentially after the spaces: "), AMOUNT_OF_NUMBERS_IN_ONE_EXPRESSION
    )

    print(
        "\n"
        f"{a1x}x {addition_or_subtraction_sign(b1y)} {abs(b1y)}y = {c1}"
        "\n"
        f"{a2x}x {addition_or_subtraction_sign(b2y)} {abs(b2y)}y = {c2}"
        "\n"
    )

    W = a1x * b2y - b1y * a2x
    Wx = c1 * b2y - b1y * c2
    Wy = a1x * c2 - c1 * a2x

    if W == Wx == Wy:
        print("The equation has infinitely many solutions")
        return True

    elif W == 0:
        print("The equation has 0 solutions")
        return False

    else:
        x = Wx / W
        y = Wy / W

        print(
            f"x = {x}"
            "\n"
            f"y = {y}"
        )

        return x, y


def calculating_system_of_equations_with_three_unknowns() -> Tuple[float, float, float] | bool:
    AMOUNT_OF_NUMBERS_IN_ONE_EXPRESSION = 4

    a1x, b1y, c1z, d1 = get_space_separated_numbers_from_text(
        input("Enter a1x b1y c1z d1 sequentially after the spaces: "), AMOUNT_OF_NUMBERS_IN_ONE_EXPRESSION
    )
    a2x, b2y, c2z, d2 = get_space_separated_numbers_from_text(
        input("Enter a2x b2y c2z d2 sequentially after the spaces: "), AMOUNT_OF_NUMBERS_IN_ONE_EXPRESSION
    )
    a3x, b3y, c3z, d3 = get_space_separated_numbers_from_text(
        input("Enter a3x b3y c3z d3 sequentially after the spaces: "), AMOUNT_OF_NUMBERS_IN_ONE_EXPRESSION
    )

    print(
        "\n"
        f"{a1x}x {addition_or_subtraction_sign(b1y)} {abs(b1y)}y {addition_or_subtraction_sign(c1z)} {abs(c1z)}z = {d1}"
        "\n"
        f"{a2x}x {addition_or_subtraction_sign(b2y)} {abs(b2y)}y {addition_or_subtraction_sign(c2z)} {abs(c2z)}z = {d2}"
        "\n"
        f"{a3x}x {addition_or_subtraction_sign(b3y)} {abs(b3y)}y {addition_or_subtraction_sign(c3z)} {abs(c3z)}z = {d3}"
        "\n"
    )

    W = a1x * b2y * c3z + b1y * c2z * a3x + c1z * a2x * b3y - b1y * a2x * c3z - a1x * c2z * b3y - c1z * b2y * a3x
    Wx = d1 * b2y * c3z + b1y * c2z * d3 + c1z * d2 * b3y - b1y * d2 * c3z - d1 * c2z * b3y - c1z * b2y * d3
    Wy = a1x * d2 * c3z + d1 * c2z * a3x + c1z * a2x * d3 - d1 * a2x * c3z - a1x * c2z * d3 - c1z * d2 * a3x
    Wz = a1x * b2y * d3 + b1y * d2 * a3x + d1 * a2x * b3y - b1y * a2x * d3 - a1x * d2 * b3y - d1 * b2y * a3x

    if W == 0 and Wx == 0 and Wy == 0 and Wz == 0:
        print("The equation has infinitely many solutions")
        return True

    elif W == 0:
        print("The equation has 0 solutions")
        return False

    else:
        x = Wx / W
        y = Wy / W
        z = Wz / W

        print(
            f"x = {x}"
            "\n"
            f"y = {y}"
            "\n"
            f"z = {z}"
        )

        return x, y, z


def main() -> None:
    choice_of_system_of_equations = input("If you want to calculate a system of equations with 2 unknowns enter 2\n"
                                          "If you want to calculate a system of equations with 3 unknowns enter 3\n"
                                          "Enter here: ")

    if choice_of_system_of_equations == "2":
        calculating_system_of_equations_with_two_unknowns()

    elif choice_of_system_of_equations == "3":
        calculating_system_of_equations_with_three_unknowns()

    else:
        raise ValueError("Entered wrong data")

    return None


if __name__ == "__main__":
    main()
