# Problem: Sort Colors (Dutch National Flag)
# Sort the array in place where values are only 0, 1, and 2.

# Input:  [1,0,2,1,0,2]
# Output: [0,0,1,1,2,2]

def sort_colors(nums):
    left = 0
    mid = 0
    right = len(nums) - 1

    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:   
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1

    return nums


nums = [1,0,2,1,0,2]  
print(sort_colors(nums))