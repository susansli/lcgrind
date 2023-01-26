# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
# such that nums[i] == nums[j] and abs(i - j) <= k.

# nums = [1,2,3,1], k = 3 --> true
# nums = [1,0,1,1], k = 1 --> true
# nums = [1,2,3,1,2,3], k = 2 --> false (since 3 > 2)

# first approach that comes to mind is to create a dictionary to store indices
# return true if the condition of <= k is met and false if end of list is reached.

def contains_dupes_ii(nums, k):
    ref = {}
    for i in range(len(nums)):
        if nums[i] not in ref:
            ref[nums[i]] = i
        else:  # curr index has to be larger than prev indices
            if i - ref[nums[i]] <= k:
                return True
            else:  # update ref
                ref[nums[i]] = i
    return False
