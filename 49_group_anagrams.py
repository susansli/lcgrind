# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# strs = ["eat","tea","tan","ate","nat","bat"]
# --> [["bat"],["nat","tan"],["ate","eat","tea"]]

# strs = [""]
# --> [[""]]

# strs = ["a"]
# [["a"]]

# Initial approach is to do a comparison of each word, but that would be awful time complexity since
# we're doing a lot of redundant comparisons.
# We can construct a dictionary where the key is a sorted string and the value an array of anagrams instead.
# Since merge sort is O(NlogN), this is a O(N^2logN) solution since we also need to loop through
# the str array.

def group_anagrams(strs):
    str_dict = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in str_dict:
            str_dict[sorted_word].append(word)
        else:
            str_dict[sorted_word] = [word]
    return list(str_dict.values())
