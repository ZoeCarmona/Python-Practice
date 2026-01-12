# Problem: Peak Element
# A peak element is an element strictly greater than its neighbors.
# Return the index of any peak element.

# You may assume:

# nums[-1] = nums[n] = -∞

# Input:  [1,2,3,1]
# Output: 2   # index of 3

def find_peak_element(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # Si el elemento del medio es menor que el de la derecha,
        # el pico está en la parte derecha
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            # El pico está en la parte izquierda (o es el mid)
            right = mid

    return left

print(find_peak_element([1,2,3,1]))