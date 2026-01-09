# Problem: Intersection of Two Arrays II
# Return the intersection of two arrays including duplicates.

# Input:  nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

def intersect(nums1, nums2):
    array = []
    count = 0

    for i in range(len(nums1)):
        print('i', i)
        for j in range(len(nums2)):
            print('j', j)
            if nums1[i] != nums2[j]:
                count = 0
                break
            count = j
    return count

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect(nums1, nums2))