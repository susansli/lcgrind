# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# [1,2,3,1] --> true
# [1,2,3,4] --> false

# 1st solution that comes to mind is to build a set and return true if it contains an existing index
# this is better than creating a list due to O(1) access time

def contains_dupes(nums):
    ref = set()  # I also checked the speed with dict and it was a lot faster
    for i in range(len(nums)):
        if nums[i] in ref:
            return True
        else:
            ref.add(nums[i])
    return False
