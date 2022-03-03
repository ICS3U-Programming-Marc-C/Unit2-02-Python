#!/usr/bin/env python3
# Created by Marc Coffi
# Created on February 2022
'''
This is a program that calculates the area and the perimeter
of a rectangle based on user input.
'''


def main():
    lenght = input("Enter a length: ")
    width = input("Enter a width: ")
    lenght = int(lenght)
    width = int(width)
    print("The Area is {}mm^2".format(lenght*width))
    print("The Perimeter is {}mm".format(2*(lenght+width)))


if __name__ == "__main__":
    main()
