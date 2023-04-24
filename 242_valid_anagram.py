# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using
# all the original letters exactly once.

# s = "anagram", t = "nagaram" --> true
# s = "rat", t = "car" --> false
# s = "ab", t = "a" --> false

# Initial approach is to create an array from all the characters in s, then loop
# through t, removing the matching character in array s if it's included.

# We can also make a dictionary for faster access time than constantly popping from an array

def is_anagram(s, t):

    if len(s) != len(t):
        return False

    s_dict = {}

    for letter in s:
        if letter in s_dict:
            s_dict[letter] += 1
        else:
            s_dict[letter] = 1

    for letter in t:
        if letter not in s_dict.keys():
            return False
        else:
            s_dict[letter] -= 1
            if s_dict[letter] == 0:
                del s_dict[letter]

    return True


print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
print(is_anagram("ab", "a"))
