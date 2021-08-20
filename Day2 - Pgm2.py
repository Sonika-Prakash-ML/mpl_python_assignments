# to find the number of zeros at the end of a factorial of a given positive number.

def find_zeros(num):
    fives = 0  # no. of 5s in the factorial
    i = 1
    while (5 ** i) <= num:
        fives += (num // (5 ** i))
        i += 1
    print("Number of trailing zeros:", fives)


if __name__ == "__main__":
    n = int(input("Enter a number:"))
    find_zeros(n)
