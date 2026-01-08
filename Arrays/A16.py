# Problem: Container With Most Water
# Given heights, return the max area of water a container can store.

# Input:  [1,8,6,2,5,4,8,3,7]
# Output: 49

def max_area(height):
    left = 0
    right = len(height) - 1
    maxArea = 0

    while left < right:
        b = right - left
        h = min(height[left], height[right])
        area = b * h
        maxArea = max(maxArea, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxArea

height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))
