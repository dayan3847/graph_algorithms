def greatest_odd_integer_which_divides_x(x: int) -> int:
    if 1 > x or 1 == x % 2:
        return -1
    while 0 == x % 2:
        x /= 2
    return int(x)


def run_greatest_odd_integer_which_divides_x():
    x: int = int(input('Insert the number of X set: '))
    y = greatest_odd_integer_which_divides_x(x)
    if -1 == y:
        print(f"The inserted value ({y}) does not belong to the set X")
    else:
        print(f"Greatest odd integer which divides x is: {y}")


if __name__ == '__main__':
    run_greatest_odd_integer_which_divides_x()
