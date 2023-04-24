# Given an integer x, return true if x is a palindrome, and false otherwise.
# x = 121 --> true
# x = -121 --> false because negatives read x- from right to left
# x = 10 --> false because 01 is not a palindrome

# Initial approach is to turn it into a string and then iterate over it
# Alternatively we can do this mathematically in a way similar to reverse_integer by constructing
# a new number and then checking equality. It would be the same as reverse_integer.

# Both time/space complexity is O(N)

def is_palindrome(x):
    if x < 0:
        return False
    string_x = str(x)
    ptr_1 = 0
    ptr_2 = len(string_x) - 1
    while ptr_1 < ptr_2:
        if string_x[ptr_1] != string_x[ptr_2]:
            return False
        ptr_1 += 1
        ptr_2 -= 1
    return True


print(is_palindrome(121))
