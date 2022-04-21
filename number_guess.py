#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in March 2022
# This is the math program, comparing the guessed number and answer

import random


def main():
    # This function calculates the number guess game
    # The game compares the guessed number and the random answer

    # input
    number_guess = input("Enter the number you guess between 0 - 9: ")

    # process & output
    answer_random = random.randint(0, 9)
    print("")
    try:
        number_integer = int(number_guess)
        if number_integer == answer_random:
            print("Your guess is right!")
        else:
            print("Your guess is wrong! The answer is {0}.".format(answer_random))
    except Exception:
        print("{} is not an integer!".format(number_guess))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
