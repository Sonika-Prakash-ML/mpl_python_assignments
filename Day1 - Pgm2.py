# to check whether the number is armstrong.

import math


def get_digits(num):
    digs = []
    temp = num
    while (temp > 0):
        d = temp % 10
        digs.append(d)
        temp = temp // 10
    return digs


def check_armstrong(num):
    digs = get_digits(num)
    n = len(digs)
    s = 0
    for i in digs:
        s += math.pow(i, n)
    if s == num:
        return True
    return False


if __name__ == "__main__":
    number = int(input("Enter a number:"))
    if check_armstrong(number):
        print("Yes")
    else:
        print("No")
