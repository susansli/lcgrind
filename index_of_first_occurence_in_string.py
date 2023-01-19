# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
# * haystack and needle consist of only lowercase English characters.

# haystack = "sadbutsad", needle = "sad" --> 0
# haystack = "leetcode", needle = "leeto" --> -1

# I would use a 2 pointer approach to solve this question. As I was doing the question I noticed the need
# to backtrack, so I used a queue.

# Note: UP TO THIS POINT this is probably one of the hardest questions due to the number of edge cases that my
# solution ended up failing; it was *extremely* confusing to keep track of the pointers especially when backtracking.
# Maybe it just means more practice is needed with the 2ptr method...

def str_str(haystack, needle):

    # The easiest way to do this is just haystack.index(needle), however we will attempt to do this
    # problem with char matching instead.

    # Looking at other solutions, maintaining a SLIDING WINDOW seems to be another solution that's much
    # cleaner and eliminates backtracking ://

    matches = []
    ptr_1 = 0
    ptr_2 = 0
    while ptr_1 + ptr_2 < len(haystack):
        if haystack[ptr_1 + ptr_2] == needle[ptr_2]:
            if ptr_2 > 0 \
                    and ptr_1 + ptr_2 not in matches \
                    and haystack[ptr_1 + ptr_2] == needle[0]:  # we only log the SECOND occurrence of needle[0]
                matches.append(ptr_1 + ptr_2)
            ptr_2 += 1
            if ptr_2 == len(needle):
                return ptr_1
        else:
            if len(matches) > 0:
                ptr_1 = matches.pop(0)
            else:
                if ptr_2 == 0:
                    ptr_1 += 1
                else:
                    ptr_1 += ptr_2
            ptr_2 = 0
    return -1