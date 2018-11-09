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

print maxSubArray([-5, -4, -3, -20, -10])
