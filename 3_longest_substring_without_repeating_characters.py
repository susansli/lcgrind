# Given a string s, find the length of the longest substring without repeating characters.
# s = "abcabcbb" --> "abc"
# s = "bbbbb" --> "b"
# s = "pwwkew" --> "wke"

# The difficult part of this question was optimization. Brute forcing would be generating every possible substring.
# A slightly better solution is to store the location of the last matched character and start counting again on the
# next character.
# However looking at the string "pwxkqweabc", the 1st substring generated would be "wxkq". The longest substring
# of this string is "xkqweabc"; the 1st part of the string intersects with the longest substring.
# Rather than move the pointer all the way back to x and then count to the 2nd w again, we can just start making
# the substring with the last matched position (w) + 1 (x) to the current w.

def length_of_longest_substring(string):
    if len(string) == 0 or len(string) == 1:
        return string

    prev_substring = ""
    curr_substring = ""
    ptr = 0
    last_match = {}

    while ptr < len(string):
        if string[ptr] not in curr_substring:
            last_match[string[ptr]] = ptr
            curr_substring = curr_substring + string[ptr]
            ptr += 1
        else:
            if len(curr_substring) > len(prev_substring):
                prev_substring = curr_substring
            curr_substring = string[last_match[string[ptr]] + 1:ptr]

    if len(prev_substring) > len(curr_substring):
        return prev_substring
    return curr_substring


print(length_of_longest_substring('dvdf'))
