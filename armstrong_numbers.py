#!/usr/bin/env python3


def get_numbers(NUM):
    """Calculate and return Armstrong numbers"""
    armstrongs = []  # Hold any Armstrong numbers found
    count = 0  # Hold number of Armstrongs found for loop condition
    test_num = 1  # Number to test whether it's an Armstrong number

    # Loop as long as we haven't found the specified amt of Armstrong numbers
    while count < int(NUM):
        bar = foo(str(test_num))  # Multiply each digit by number of digits

        if bar == test_num:
            count += 1
            armstrongs.append(bar)
        test_num += 1

    print(armstrongs)


def foo(test_num):
    """Multiply each digit by the number of digits"""
    total = 0
    digits = len(test_num)

    for digit in range(digits):
        total += int(test_num[digit]) ** digits
    return total


def __main__():
    NUM = "13"  # How many Armstrong numbers to find
    get_numbers(NUM)


if __name__ == "__main__":
    __main__()
