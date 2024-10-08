#!/usr/bin/python3
""" solution module """


def canUnlockAll(boxes):
    """ Returns true if all boxes can be unlocked, false otherwise"""
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys_to_try = boxes[0]

    while keys_to_try:
        new_keys_to_try = []
        for key in keys_to_try:
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                new_keys_to_try.extend(boxes[key])
        keys_to_try = new_keys_to_try

    return (all(unlocked))
