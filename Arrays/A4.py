# Problem
# Move all 0s to the end of the array while maintaining the order of non-zero elements.

# Example

# Input:  [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

def move_zeros(nums):
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    
    return nums

nums = [0, 1, 0, 3, 12]
print(move_zeros(nums))
