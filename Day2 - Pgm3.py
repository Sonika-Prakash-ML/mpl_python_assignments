# to find the digits which are absent in a given mobile number.

def get_nums(p_nums):
    all_nums = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    a_nums = all_nums.difference(p_nums)
    print("The digits which are absent are:", *a_nums)


if __name__ == "__main__":
    mbl = set(list(map(int, input("Enter the mobile number:"))))
    get_nums(mbl)
    