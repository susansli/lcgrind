def palindrome(s):

    if len(s) <= 1:
        return s

    longest_sub = s[0]

    for i in range(len(s) - 1):
        sub = ''
        if i + 1 <= len(s) - 1 and s[i] == s[i + 1]:  # even palindromes
            sub = return_sub(s[i] + s[i + 1], s, i - 1, i + 2)
        if (i - 1 >= 0 and i + 1 <= len(s) - 1) and \
                s[i - 1] == s[i + 1]:  # odd palindromes
            sub = return_sub(s[i - 1] + s[i] + s[i + 1], s, i - 2, i + 2)
        if len(sub) > len(longest_sub):
            longest_sub = sub
    return longest_sub


def return_sub(sub, s, start, end):
    while (start >= 0 and end <= len(s) - 1) and \
            s[start] == s[end]:
        sub = sub + s[end]
        sub = s[start] + sub
        start -= 1
        end += 1
    return sub


print(palindrome('aaaaa'))
