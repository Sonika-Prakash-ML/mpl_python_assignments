# to print a pattern

def disp_pattern(r):
    # for upper part
    for i in range(1, r + 1):
        for j in range(1, i):
            print(" ", end="")
        for k in range(i, r + 1):
            print("*", end=" ")
        print()

    # for lower part
    for i in range(r - 1, 0, -1):
        for j in range(1, i):
            print(" ", end="")
        for k in range(i, r + 1):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    rows = int(input("Enter the number of rows:"))
    disp_pattern(rows)
