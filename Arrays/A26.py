# Problem: Intersection of Two Arrays II
# Return the intersection of two arrays including duplicates.

# Input:  nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

def intersect(nums1, nums2):
    freq = {}
    for x in nums1:
        freq[x] = freq.get(x, 0) + 1

    result = []
    for y in nums2:
        if freq.get(y, 0) > 0:
            result.append(y)
            freq[y] -= 1

    return result


nums1 = [1, 2]
nums2 = [2, 2, 2, 2]

print(intersect(nums1, nums2))