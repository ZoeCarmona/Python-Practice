# Problem
# Given a sorted array, remove duplicates in place and return the new length.

# Input:  [1,1,2,2,3] 
# Output: 3  array becomes [1,2,3,_ ,_]
def remove_duplicates(nums):
    if not nums:
        return 0

    left = 1  # el primer elemento siempre es único

    for right in range(1, len(nums)):
        # print('Left es ', left)
        # print('R es ', right)
        if nums[right] != nums[left - 1]:
            nums[left] = nums[right]
            # print(nums)
            left += 1

    return left

nums = [1,1,2,2,3]
print(remove_duplicates(nums), nums)

