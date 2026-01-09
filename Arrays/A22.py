# Problem: Minimum Size Subarray Sum
# Given an array of positive integers and a target s, return the minimum length of a contiguous subarray whose sum is at least s.
# If no such subarray exists, return 0.

# Input:  nums = [2,3,1,2,4,3], s = 7
# Output: 2   # [4,3]

def min_subarray_len(s, nums):
    left = 0
    sumWindow = 0
    best = float("inf")

    for right in range(len(nums)):
        sumWindow += nums[right]
        while sumWindow >= s:
            best = min(best, right - left + 1)
            sumWindow -= nums[left]
            left += 1

    return 0 if best == float("inf") else best

nums = [2,3,1,2,4,3]
s = 7
print(min_subarray_len(s,nums))