# Problem: Find First Duplicate
# Return the first duplicate number you encounter while scanning from left to right.

# Input:  [2, 1, 3, 5, 3, 2]
# Output: 3
def first_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return n
        seen.add(n)
nums = [2, 1, 3, 5, 4, 6]
print(first_duplicate(nums))