def findMin(nums):
    max = len(nums) - 1
    min = 0
    middle = (min + max) / 2

    while max >= min:
        if max == min:
            return nums[min]
        elif nums[middle - 1] > nums[middle]:
            return nums[middle]
        elif nums[middle] > nums[middle + 1]:
            return nums[middle + 1]
        elif nums[min] > nums[max] and nums[min] < nums[middle]:
            min = middle + 1
        else:
            max = middle - 1
        middle = (min + max) / 2


print findMin([1,2,3,4,5,6])
print findMin([2,3,4,5,6,1])
print findMin([3,4,5,6,1,2])
print findMin([4,5,6,1,2,3])
print findMin([5,6,1,2,3,4])
print findMin([6,1,2,3,4,5])
print findMin([2, 0, 1])
#print findMin([1])