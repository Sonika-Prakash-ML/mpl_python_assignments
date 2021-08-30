#  to interchange 2nd and 4th elements in a list.

def interchange(lst):
    try:
        lst[1], lst[3] = lst[3], lst[1]
        print("The resultant list is:", lst)
    except:
        print("The list size is less than 4!")


if __name__ == "__main__":
    lst = list(map(int, input("Enter the elements of list:").split()))
    print("The original list is:", lst)
    interchange(lst)
