#!/usr/bin/python3
"""
minimum operations that obtain n occurences of a character
"""


def minOperations(n):
    """
    Calculates the fewest number of occurences of a character in a file

    Args:
    n: Number of H characters to be achieved

    Returns:
    Integer representing the fewest numbe of operations occured.
    0 if n is impossible to achieve
    """

    if n < 2:
        return 0

    occurences = 1
    current = 2

    for i in range(2, n + 1):
        if current * 2 <= i:
            occurences += 1
            current *= 2
        else:
            occurences += 1
            current += current - 1

    return occurences
