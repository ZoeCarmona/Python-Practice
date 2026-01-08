# Problem: Majority Element
# Return the element that appears more than ⌊n/2⌋ times.

# Input:  [3,2,3]
# Output: 3

def majority_element(nums):
    seen = {}
    threshold = len(nums) // 2

    for n in nums:
        seen[n] = seen.get(n, 0) + 1
        if seen[n] > threshold:
            return n

nums = [3,2,1]
print(majority_element(nums))