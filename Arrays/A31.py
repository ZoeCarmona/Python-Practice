# Problem: Squares of a Sorted Array
# Given a sorted array (can include negatives), return a sorted array of their squares.

# Input:  [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

def sorted_squares(nums):
    n = len(nums)
    res = [0] * n
    left, right = 0, n - 1
    pos = n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            res[pos] = nums[left] * nums[left]
            left += 1
        else:
            res[pos] = nums[right] * nums[right]
            right -= 1
        pos -= 1

    return res

print(sorted_squares([-4,-1,0,3,10]))