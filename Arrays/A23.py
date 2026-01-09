# Problem: Find All Duplicates in an Array
# Array has integers from 1 to n.
# Some appear twice, others once.
# Return all elements that appear twice.

# Input:  [4,3,2,7,8,2,3,1]
# Output: [2,3]

def find_duplicates(nums):
    seen = {}
    array = []

    for n in nums:
        seen[n] = seen.get(n, 0) + 1

    for n in nums:
        if seen[n] == 2:
            array.append(n)
            seen[n] -= 1
    
    # for n in nums:
    #     idx = abs(n) - 1
    #     if nums[idx] < 0:
    #         res.append(abs(n))
    #     else:
    #         nums[idx] = -nums[idx]
    
    return array

nums = [4,3,2,7,8,2,3,1]
print(find_duplicates(nums))