def main():
    x, y = get_fuel()
    print(f"{x}/{y}")

def get_fuel():
    while True:
        try:
            x, y = map(int, input().split("/"))
        except ValueError:
            print("Invalid input. Enter two integers separated by '/'.")
            continue

        if y == 0 or x > y:
            print("Invalid fraction: x must be <= y and y must not be 0.")
            continue

        return x, y

if __name__ == "__main__":
    main()