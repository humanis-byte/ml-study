def main():
    x, y = get_fuel()
    print(f"{x}/{y}")


def get_fuel():
    while True:
        try:
            x, y = map(int, input().split("/"))
            return x, y if x <= y and y != 0 else None
        except ValueError:
            print("Invalid input. Please enter two integers or enter x  <= y.")
        except ZeroDivisionError:
            print("Denominator cannot be zero. Please enter a valid fraction.")
