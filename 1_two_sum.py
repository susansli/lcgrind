# July 2021: when I discovered leetcode was hard ;__;
# Really crazy how far you come in a few years...

def two_sum(nums, target):
    reference = {}
    for i in range(len(nums)):
        if nums[i] in reference:
            return [i, reference[nums[i]]]
        else:
            reference[target - nums[i]] = i
