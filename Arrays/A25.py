# Problem: Check If Array Is Monotonic
# Return True if the array is entirely non-increasing or non-decreasing.

# Input:  [1,2,2,3]
# Output: True

def is_monotonic(nums):
    inc = True
    dec = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            inc = False
        if nums[i] > nums[i - 1]:
            dec = False

    return inc or dec

nums = [1,2,2,3]
print(is_monotonic(nums))