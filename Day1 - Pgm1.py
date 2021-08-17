#  to interchange 2nd and 4th elements in a list.

def interchange(lst):
    temp = lst[1]
    lst[1] = lst[3]
    lst[3] = temp
    print("The resultant list is:", lst)


if __name__ == "__main__":
    lst = list(map(int, input("Enter the elements of list:").split()))
    print("The original list is:", lst)
    interchange(lst)
