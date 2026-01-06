# Problem: Missing Number
# Array contains numbers from 0 to n, one is missing.

# Input:  [3,0,1]
# Output: 2
def missing_number(nums):
    seen = set(nums)      
    n = len(nums)         

    for x in range(n + 1):
        if x not in seen:
            return x

nums = [0,1,2]
print(missing_number(nums))