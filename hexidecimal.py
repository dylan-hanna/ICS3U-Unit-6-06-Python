#!/usr/bin/env python3

# Created by Dylan Hanna
# Created on December 2019
# This program Translates Hexadecimal to Unicode


def unicode_conversion(single_char):
    # This function converts the character to a hexadecimal

    conversion = {}

    conversion[' '] = "20"
    conversion['a'] = "61"
    conversion['b'] = "62"
    conversion['c'] = "63"
    conversion['d'] = "64"
    conversion['e'] = "65"
    conversion['f'] = "66"
    conversion['g'] = "67"
    conversion['h'] = "68"
    conversion['i'] = "69"
    conversion['j'] = "6a"
    conversion['k'] = "6b"
    conversion['l'] = "6c"
    conversion['m'] = "6d"
    conversion['n'] = "6e"
    conversion['o'] = "6f"
    conversion['p'] = "70"
    conversion['q'] = "71"
    conversion['r'] = "72"
    conversion['s'] = "73"
    conversion['t'] = "74"
    conversion['u'] = "75"
    conversion['v'] = "76"
    conversion['w'] = "77"
    conversion['x'] = "78"
    conversion['y'] = "79"
    conversion['z'] = "7a"

    # return the hex code for the character
    if single_char in conversion.keys():
        return conversion[single_char]
    else:
        return -1


def main():
    # This function takes input from user
    word_string = input("Enter a Word(Small Letters): ")
    for single_element in word_string:
        answer = unicode_conversion(single_element)
        print("Unicode is: {0} - {1} ".format(single_element, answer))


if __name__ == "__main__":
    main()
