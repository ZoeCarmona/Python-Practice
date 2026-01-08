# Problem: Longest Increasing Subarray
# Return the length of the longest contiguous strictly increasing subarray.

# Input:  [1, 3, 5, 4, 7]
# Output: 3   # [1,3,5]

def longest_increasing_subarray(nums):
    if not nums:
        return 0

    max_len = 1
    curr_len = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1

    return max_len

nums = [100, 1, 2, 3, 4, 5, 6, 7, 0]
print(longest_increasing_subarray(nums))