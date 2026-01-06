# Problem 9: Reverse Subarray
# Reverse the array between two indices left and right.

# Input: nums=[1,2,3,4,5], left=1, right=3
# Output: [1,4,3,2,5]

def reverse_subarray(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums

nums = [1,2,3,4,5]
print(reverse_subarray(nums, 1,3))