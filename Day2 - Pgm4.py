# to reverse the digits of a given number and add it to the original.

def get_reverse(num):
    temp = num
    rev = 0
    while num > 0:
        dig = num % 10
        rev = (rev * 10) + dig
        num = num // 10
    if rev == temp:
        flag = True
    else:
        flag = False
    return rev, flag


def get_result(num):
    rnum, palindrome = get_reverse(num)
    # print(rnum, palindrome)
    snum = rnum + num
    # print(snum)
    while(True):
        rnum, palindrome = get_reverse(snum)
        if palindrome:
            break
        snum += rnum
    print("Result:", snum)


if __name__ == "__main__":
    num = int(input("Enter a number in the range 100 to 10000:"))
    if num >= 100 and num <= 10000:
        get_result(num)
    else:
        print("Number out of range!")
