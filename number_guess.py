#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in March 2022
# This is the math program, comparing the guessed number and answer

import random


def main():
    # This function calculates the number guess game
    # The game compares the guessed number and the random answer

    # input
    # process & output
    answer_random = random.randint(0, 9)
    while True:
        print("")
        guess_string = input("Enter the number you guess between 0 - 9: ")
        print("")
        try:
            guess_integer = int(guess_string)
            if guess_integer < 0 or guess_integer > 9:
                print("Please put in a number between 0 and 9!")
                print("Please try again.")
            elif guess_integer < answer_random:
                print("The answer is bigger than your number!")
                print("Please try again.")
            elif guess_integer > answer_random:
                print("The answer is smaller than your number!")
                print("Please try again.")
            else:
                print("Your guess is right! The answer is {}!".format(answer_random))
                print("\nDone.")
                break
        except Exception:
            print("Invalid number!")
            print("Please try again.")


if __name__ == "__main__":
    main()
