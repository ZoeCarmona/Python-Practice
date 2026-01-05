# Problem
# Given an array of integers and a target value, return the indices of the two numbers that add up to the target.

# Example

# Input:  nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

def two_sum(nums, target):
    result = []
    left = 0
    rigth = 0

    for n in range(len(nums)):
        indexX = n
        search = target - nums[n]
        
        if search < 0:
            rigth += 1
        elif search >= 0:
            rigth += 1
            indexY = rigth
            y = nums[rigth]

            sum = nums[n] + y 

            if sum == target:
                result.append(n)
                result.append(rigth)

    return result

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))