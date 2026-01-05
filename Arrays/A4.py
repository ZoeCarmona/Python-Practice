# Problem
# Move all 0s to the end of the array while maintaining the order of non-zero elements.

# Example

# Input:  [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

def move_zeros(nums):
    array = []
    temp = len(nums) -1

    for n in range(len(nums)):
        if nums[n] == 0:
            array.append(n)
    for n in array:
        print(n)
        nums[n], nums[temp] = nums[temp], nums[n]
        temp -= 1

    return nums

nums = [0, 1, 0, 3, 12]
print(move_zeros(nums))
