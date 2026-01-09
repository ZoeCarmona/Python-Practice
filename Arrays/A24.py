# Problem: Maximum Product of Two Elements
# Return the maximum product of two different elements in the array.

# Input:  [3,4,5,2]
# Output: 20   # 4 * 5

def max_product(nums):
    if len(nums) < 2:
        return None

    first = second = float('-inf')

    for n in nums:
        if n > first:
            second = first
            first = n
        elif n > second:
            second = n

    return first * second

nums = [3,4,5,2]
print(max_product(nums))