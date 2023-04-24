# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

# It is guaranteed that the answer is unique.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# nums = [1,1,1,2,2,3], k = 2 --> [1,2]
# nums = [1], k = 1 --> [1]

# We can do this by creating a dictionary to log frequencies. After that, we can sort by frequencies, and
# create an array from the keys. This fits the time complexity requirement, since sorting will take O(NlogN)

# Tip from Oscar: use bucket sort to get O(N) time at the expense of space

# Other ways to solve: max heap, O(klogN) time, better than NlogN as long as k < N

def top_k_frequent(nums, k):
    frequencies = {}
    for num in nums:
        if num in frequencies:
            frequencies[num] += 1
        else:
            frequencies[num] = 1
    # list comp of first k keys after sorting frequencies by value
    return [k for k, v in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)][:k]


def top_k_freq_bucket_sort(nums, k):
    # 1. Create a dictionary of frequencies (same as solution 1)
    # 2. Create a 2D list to represent buckets of the bucket sort
    # 3. Populate the buckets with the frequencies dictionary
    # 4. Reverse the 2D list, appending values if they exist to a new list to return
    # 5. Slice the list meant for return to the kth element
    # This results in O(N) time at a space tradeoff

    frequencies = {}
    for num in nums:
        if num in frequencies:
            frequencies[num] += 1
        else:
            frequencies[num] = 1

    buckets = [[] for _ in range(len(nums))]

    for key, value in frequencies.items():
        buckets[value].append(key)

    output = []

    for value in reversed(buckets):
        # to merge lists, just += the lists together
        output += value

    return output[:k]

