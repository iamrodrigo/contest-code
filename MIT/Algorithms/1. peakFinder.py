class Solution(object):
    def findPeakElement(self, nums):
        minN = 0
        maxN = len(nums) - 1
        middle = 0

        if len(nums) == 1:
            return middle

        while maxN >= minN:
            middle = minN + ((maxN - minN) / 2)

            if (middle != minN != maxN and nums[middle] > nums[middle - 1] and nums[middle] > nums[
                middle + 1]) or (minN == maxN == 0 and nums[middle] > nums[middle + 1]) or (
                    minN == maxN == len(nums) - 1 and nums[middle] > nums[middle - 1]):
                break
            elif nums[middle + 1] > nums[middle]:
                minN = middle + 1
            else:
                maxN = middle - 1

        return middle