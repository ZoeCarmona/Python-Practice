# Problem: Subarray Sum Equals K
# Return the number of continuous subarrays whose sum equals k.

# Input: nums = [1,1,1], k = 2
# Only for positive numbers
# Output: 2

def subarray_sum(nums, k):
    left = 0
    rigth = 0
    sumWindow = 0
    count = 0

    for n in range(len(nums)):
        sumWindow += nums[n]

        if sumWindow == k:
            count += 1
            sumWindow -= nums[left]
            left += 1
        
        rigth += 1
    return count

nums = [1,1,1]
k = 2
print(subarray_sum(nums, k))
