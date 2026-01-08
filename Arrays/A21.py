# Problem: Longest Consecutive Sequence
# Return the length of the longest sequence of consecutive integers.

# Input:  [100,4,200,1,3,2]
# Output: 4   # [1,2,3,4]

def longest_consecutive(nums):
    s = set(nums)
    best = 0

    for x in s:
        if x - 1 not in s:
            length = 1
            while x + length in s:
                length += 1
            best = max(best, length)

    return best


nums = [100,4,200,1,3,2,2]
print(longest_consecutive(nums))