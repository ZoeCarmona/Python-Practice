# Problem: Count Even Numbers
# Return how many numbers in the array are even.

# Input:  [1, 2, 3, 4, 6]
# Output: 3
def count_evens(nums):
    count = 0
    for n in nums:
        if n % 2 == 0: count +=1
    return count

nums = [1, 2, 3, 4, 6]
print(count_evens(nums))

