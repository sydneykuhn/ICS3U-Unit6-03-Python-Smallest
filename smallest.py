#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Oct 2020
# This program finds the smallest of 10 random numbers

import random


def find_smallest(list_of_numbers):
    # this function finds the smallest number in a list

    smallest = list_of_numbers[9]

    for loop_item in list_of_numbers:
        if loop_item < smallest:
            smallest = loop_item
        else:
            smallest = smallest

    return smallest


def main():
    # this function creates 10 random numbers in a list

    list_of_numbers = []

    # input
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)  # a number between 1-100
        list_of_numbers.append(random_number)
        print("The random number is : {0}".format(random_number))
        loop_counter += 1

    smallest_number = find_smallest(list_of_numbers)

    print("\n\nThe smallest number is {0}".format(smallest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
