def maxSubArray(nums):
    total = 0
    max = nums[0]

    for i, n in enumerate(nums):
        total += n

        if total > max:
            max = total

        if total < 0:
            total = 0

    return max

def maxSubArrayII(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)

a = [-2,1,-3,4,-1,2,1,-5,4]

print maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print maxSubArrayII([-2,1,-3,4,-1,2,1,-5,4])