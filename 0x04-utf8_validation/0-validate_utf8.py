#!/usr/bin/python3
""" validate utf-8 encoding"""


def validUTF8(data):
    """ checks if {data} is valid """

    for item in data:
        byte_list = []
        while item > 0:
            byte_list.insert(0, item & 0xFF)
            item >>= 8

        i = 0
        while i < len(byte_list):
            byte = byte_list[i]

            if byte & 0b10000000 == 0:
                i += 1
                continue

            elif byte & 0b11100000 == 0b11000000:
                if (i + 1 >= len(byte_list) or
                   (byte_list[i + 1] & 0b11000000) != 0b10000000):
                    return False
                i += 2

            elif byte & 0b11110000 == 0b11100000:
                if (i + 2 >= len(byte_list) or
                   (byte_list[i + 1] & 0b11000000) != 0b10000000 or
                   (byte_list[i + 2] & 0b11000000) != 0b10000000):
                    return False
                i += 3

            elif byte & 0b11111000 == 0b11110000:
                if (i + 3 >= len(byte_list) or
                   (byte_list[i + 1] & 0b11000000) != 0b10000000 or
                   (byte_list[i + 2] & 0b11000000) != 0b10000000 or
                   (byte_list[i + 3] & 0b11000000) != 0b10000000):
                    return False
                i += 4

            else:
                return False
        return True
