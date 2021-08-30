# to sort dictionary by key or value

def dict_sort(dct, s):
    print("{", end='')
    if s == 0:
        for k, v in sorted(dct.items(), key=lambda x: x[0]):
            print(k,":", v, end=", ")
    elif s == 1:
        for k, v in sorted(dct.items(), key=lambda x: x[1]):
            print(k, ":", v, end=", ")
    print("}")


if __name__ == "__main__":
    dct = dict()
    print("Enter the key-value pairs separated by space on each line. Press 'q' when done.")
    while True:
        inp = input().split()
        if inp[0] == 'q':
            break
        else:
            inp = list(map(int, inp))
            dct[inp[0]] = inp[1]
    print("The dictionary is:", dct)
    s = int(input("Press 0 to sort by key, and 1 to sort by value:"))
    dict_sort(dct, s)
