# Problem: Second Largest Element
# Return the second largest number in the array.

# Input:  [10, 5, 20, 8]
# Output: 10

# No sorting allowed.
def second_largest(nums):
    if len(nums) < 2:
        return None

    first = float("-inf")
    second = float("-inf")

    for x in nums:
        if x > first:
            second = first
            first = x
        elif first > x > second:   # distinct
            second = x

    return None if second == float("-inf") else second

nums = [10, 5, 20, 8]
print(second_largest(nums))