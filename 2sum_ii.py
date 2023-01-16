# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers
# such that they add up to a specific target number

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2]
# of length 2.

# Space complexity must be O(1)

# My approach is to go through each element of the list to find a target number, then binary search the rest of
# the list to see if it exists.

# The time complexity of this solution is O(NlogN), however it uses constant space O(1)

# After looking at LC: a faster way to solve this in O(N) time is to use 2 pointers, since the list is already
# sorted, if p1 + p2 is larger than target, move p2 left (decreasing the sum). If it's smaller than target then
# move p1 right (increasing the sum). Repeat until p1 + p2 = target.

def two_sum(numbers, target):
    for i in range(len(numbers)):
        remainder = target - numbers[i]
        remainder_index = binary_search(numbers, remainder, i + 1, len(numbers) - 1)
        if remainder_index > -1:
            return [i + 1, remainder_index + 1]
    return []


def binary_search(lst, target, low, high):
    if high >= low:
        mid = (high + low) // 2  # in cases of a list of len 1, floor division returns 0
        if lst[mid] == target:
            return mid
        elif target > lst[mid]:
            return binary_search(lst, target, mid + 1, high)
        else:
            return binary_search(lst, target, low, mid - 1)
    else:
        return -1


print(two_sum([5, 25, 75], 100))
