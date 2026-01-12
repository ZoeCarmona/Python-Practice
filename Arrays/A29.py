# Problem: Shortest Unsorted Continuous Subarray
# Return the length of the shortest subarray which, if sorted, results in the whole array being sorted.

# Input:  [2,6,4,8,10,9,15]
# Output: 5   # sort [6,4,8,10,9]

def find_unsorted_subarray(nums):
    n = len(nums)
    left = 0

    while left < n - 1 and nums[left] <= nums[left + 1]:
        left += 1
    if left == n - 1:
        return 0  
    
    right = n - 1
    
    while right > 0 and nums[right - 1] <= nums[right]:
        right -= 1

    sub_min = min(nums[left:right + 1])
    sub_max = max(nums[left:right + 1])

    while left > 0 and nums[left - 1] > sub_min:
        left -= 1

    while right < n - 1 and nums[right + 1] < sub_max:
        right += 1

    return right - left + 1

print(find_unsorted_subarray([2,6,4,8,10,9,15]))