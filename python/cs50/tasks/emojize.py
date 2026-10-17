import emoji
import msvcrt

while True:
    emoj = str(input("Input: "))
    print(emoji.emojize(f"Output: {emoj}"))

    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'q':
            break

