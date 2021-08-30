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
    if snum >= 100 and snum <= 10000:
        print("Result:", snum)
    else:
        print("No such number within the range 100 - 10000.")
