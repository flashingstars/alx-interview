#!/usr/bin/python3
""" Function that returns a boolean answer when all boxes are locked or unlocked """


def canUnlockAll(boxes):
    """ Function to unlock boxes """
    n = len(boxes) # Finding total box number
    unlocked = [False] * n
    unlocked[0] = True # First box is unlocked

    keys = boxes[0]

    """ Iterating through the available keys """
    while keys:
        key = keys.pop()

        if key < n and not unlocked[key]:
            """ If key corresponds to box, unlock and add keys to unlocked"""
            unlocked[key] = True
            keys.extend(boxes[key])

    return all(unlocked)
