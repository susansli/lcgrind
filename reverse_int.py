# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

# 123 --> 321
# -123 --> -321
# 120 --> 21
# 504 --> 405

# Initial thought is to turn the number into a string and reverse the string. The time complexity would be O(N)
# We can also do this mathematically, which would be substantially faster than string operations. However, it
# does make the code a bit harder to read. Both time/space complexity is O(N).

MIN = -2 ** 31
MAX = 2 ** 31 - 1


def reverse(x):
    x_abs = abs(x)
    reverse_int = 0

    while x_abs != 0:
        reverse_int *= 10
        curr_dig = x_abs - ((x_abs // 10) * 10)
        reverse_int += curr_dig
        x_abs = (x_abs - curr_dig) / 10

    reverse_int = int(reverse_int)  # floor division turns the number into a float :(

    if reverse_int > MAX or reverse_int < MIN:
        return 0
    if x < 0:
        return -1 * reverse_int
    return reverse_int

