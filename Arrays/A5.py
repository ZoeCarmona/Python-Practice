# Problem: Two Sum (Index)
# Given an array of integers and a target value, return the indices of the two numbers that add up to the target.

# Example

# Input:  nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

def two_sum(nums, target):
    seen = {}

    for i, n in enumerate(nums):
        search = target - n

        if search in seen:
            return [seen[search], i]

        seen[n] = i
    


nums = [2, 7, 11, 15, 2]
target = 9
print(two_sum(nums, target))