import math

wybor = input("Jeżeli chcesz obliczyć układ równań z 2 niewiadomymi wpisz 2\n"
              "Jeżeli chcesz obliczyć układ równań z 3 niewiadomymi wpisz 3\n"
              "Wpisz tutaj: ")

if wybor == "2":

    def pobierz_3_floaty(instrukcja):
        tekst = input(instrukcja)
        czesci = tekst.split()
        ax, by, c = [float(i) for i in czesci]
        if not (math.isfinite(ax) and math.isfinite(by) and math.isfinite(c)):
            raise ValueError("Podano nieskończoność")
        return ax, by, c

    try:
        a1x, b1y, c1 = pobierz_3_floaty("Wprowadź po spacji kolejno a1x b1y c1: ")
        a2x, b2y, c2 = pobierz_3_floaty("Wprowadź po spacji kolejno a2x a2y c2: ")

    except ValueError as error:
        print("\nBŁĄD\n")
        print(f"Powód błędu: {error}")
        exit()

    else:
        print()

        def plus_minus(znak):
            return "-" if znak < 0 else "+"

        print(f"{a1x}x {plus_minus(b1y)} {abs(b1y)}y = {c1}")
        print(f"{a2x}x {plus_minus(b2y)} {abs(b2y)}y = {c2}\n")

        W = a1x * b2y - b1y * a2x
        Wx = c1 * b2y - b1y * c2
        Wy = a1x * c2 - c1 * a2x

        if W == Wx == Wy:
            print("Równanie ma nieskończenie wiele rozwiązań")
        elif Wx != 0 and Wy != 0 and W == 0:
            print("Równanie ma 0 rozwiązań")
        else:
            x = Wx / W
            y = Wy / W

            print(f"x = {x}")
            print(f"y = {y}")

elif wybor == "3":

    def pobierz_4_floaty(instrukcja):
        tekst = input(instrukcja)
        czesci = tekst.split()
        ax, by, cz, d = [float(i) for i in czesci]
        if not (math.isfinite(ax) and math.isfinite(by) and math.isfinite(cz) and math.isfinite(d)):
            raise ValueError("Podano nieskończoność")
        return ax, by, cz, d

    try:
        a1x, b1y, c1z, d1 = pobierz_4_floaty("Wprowadź po spacji kolejno a1x b1y c1z d1: ")
        a2x, b2y, c2z, d2 = pobierz_4_floaty("Wprowadź po spacji kolejno a2x a2y c2z d2: ")
        a3x, b3y, c3z, d3 = pobierz_4_floaty("Wprowadź po spacji kolejno a3x b3y c3z d3: ")

    except ValueError as error:
        print("\nBŁĄD\n")
        print(f"Powód błędu: {error}")
        exit()

    else:
        print()

        def plus_minus(znak):
            return "-" if znak < 0 else "+"

        print(f"{a1x}x {plus_minus(b1y)} {abs(b1y)}y {plus_minus(c1z)} {abs(c1z)}z = {d1}")
        print(f"{a2x}x {plus_minus(b2y)} {abs(b2y)}y {plus_minus(c2z)} {abs(c2z)}z = {d2}")
        print(f"{a3x}x {plus_minus(b3y)} {abs(b3y)}y {plus_minus(c3z)} {abs(c3z)}z = {d3}\n")

        W = a1x * b2y * c3z + b1y * c2z * a3x + c1z * a2x * b3y - b1y * a2x * c3z - a1x * c2z * b3y - c1z * b2y * a3x
        Wx = d1 * b2y * c3z + b1y * c2z * d3 + c1z * d2 * b3y - b1y * d2 * c3z - d1 * c2z * b3y - c1z * b2y * d3
        Wy = a1x * d2 * c3z + d1 * c2z * a3x + c1z * a2x * d3 - d1 * a2x * c3z - a1x * c2z * d3 - c1z * d2 * a3x
        Wz = a1x * b2y * d3 + b1y * d2 * a3x + d1 * a2x * b3y - b1y * a2x * d3 - a1x * d2 * b3y - d1 * b2y * a3x

        if W == 0 and Wx == 0 and Wy == 0 and Wz == 0:
            print("Równanie ma nieskończenie wiele rozwiązań")
        elif W == 0 and (Wx or Wy or Wz) != 0:
            print("Równanie ma 0 rozwiązań")
        else:
            x = Wx / W
            y = Wy / W
            z = Wz / W

            print(f"x = {x}")
            print(f"y = {y}")
            print(f"z = {z}")

else:
    print("\nPodałeś błędne informacje")
