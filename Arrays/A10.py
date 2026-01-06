# Problem 10
# Return the maximum sum of any subarray of size k.

# Input: nums=[2,1,5,1,3,2], k=3
# Output: 9   # [5,1,3]
def max_subarray_sum(nums, k):
    left = 0
    right = k 
    sum = 0
    
    if k <= 0 or k > len(nums):
        return None

    for n in range(right):
        sum += nums[n]

    maxSum = sum

    for n in range(k, len(nums)):
        sum += nums[n]
        sum -= nums[left]

        if(sum >= maxSum):
            maxSum = sum
        
        left +=1

    return maxSum

nums=[2,1,5,1,3,2]
k = 3
print(max_subarray_sum(nums, k))