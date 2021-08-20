# to find the median among three given numbers.

def get_median(nums):
    nums.sort()
    print("The median is:", nums[1])


if __name__ == "__main__":
    nums = []
    for i in range(3):
        print("Enter number -", i + 1, ":")
        nums.append(int(input()))
    get_median(nums)