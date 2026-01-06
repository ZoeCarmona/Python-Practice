# Problem
# Return an array where each element is the running sum.

# Input:  [1,2,3,4,5]
# Output: [1,3,6,10,15]
def running_sum(nums):
    sum = nums[0]
    for n in range(1, len(nums)):
        sum += nums[n]
        nums[n] = sum
    return nums

nums = [1,2,3,4,5]
print(running_sum(nums))