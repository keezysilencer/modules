__author__ = "Keezy Silencer"
import cmath
import sys


def calc():
    # Take value of co-efficients
    a = int(input("Enter the co-efficient of a: "))
    b = int(input("Enter the co-efficient of b: "))
    c = int(input("Enter the co-efficient of c: "))

    # calculate the discriminate
    d = (b ** 2) - (4 * a * c)

    # find the value of x1 and x2
    x1 = (-b - cmath.sqrt(d)) / (2 * a)
    x2 = (-b + cmath.sqrt(d)) / (2 * a)

    # print solution to screen
    print("The solutions are {0} and {1}".format(x1, x2))


if __name__ == '__main__':
    calc()
