# to print fibonacci series using recursion between n1 and n2

def get_fib(first, second, limit):
    if second == limit:
        return
    elif (first + second) > limit:
        return
    else:
        print(first + second, end=", ")
    return get_fib(second, first + second, limit)


if __name__ == "__main__":
    n1 = int(input("Enter the first number:"))
    n2 = int(input("Enter the second number:"))
    first = n1
    second = n1 + 1
    print(first, ",", second, end=", ")
    get_fib(first, second, n2)
