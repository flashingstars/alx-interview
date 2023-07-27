#!/usr/bin/python3
"""
Function that checks if data represents a valid utf8 character
"""


def validUTF8(data):
    """
    Function that determines whether the given data is utf-8 compliant.

    Args:
        data (data): Multiple characters represented by a list of integers.
    Returns:
        bool: True if data is a valid UTF-8 integer, otherwise False.
    """
    counter = 0

    # Iterate through each integer in the list
    for num in data:
        # If counter is 0, check the number of leading 1's present
        if counter == 0:
            if (num >> 5) == 0b110:
                counter = 1
            elif (num >> 4) == 0b1110:
                counter = 2
            elif (num >> 3) == 0b11110:
                counter = 3
            elif (num >> 7) != 0:
                return False
        # If counter is not 0, check if the current integer is a valid byte
        else:
            if (num >> 6) != 0b10:
                return False
            counter -= 1

    # A valid counter is 0 after iterating through all the integers
    return counter == 0
