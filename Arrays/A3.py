# Problem
# Reverse the array in place (do not create a new array).
# Do not use reverse() or slicing.

# Example

# Input:  [1, 2, 3, 4]
# Output: [4, 3, 2, 1]

def reverse_array(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums

nums = [1, 2, 3, 4]
print(reverse_array(nums))


