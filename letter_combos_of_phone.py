# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
# could represent. Return the answer in any order. 1 matches to nothing.

# "23" --> ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# "237" --> ["adp", "adq", "adr", "ads" ... "cfp", "cfq", "cfr", "cfs"]
# "" -> []
# "2" -> ["a","b","c"]

# My approach would be to create a dictionary of the different letters the numbers match to.
# Then I would create different combinations with that dictionary.

# When creating combinations: first, recursively run function until base case is reached.
# The base case is the first letter of the combination, like "a" in "abc".
# On each subsequent recursive step append the next letter and create a new array, throwing
# away the old one. [a, b, c] --> [ad, bd, cd, ae, ...]
# ** To create permutations, prepend AND append the letter.

letter_ref = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


def letter_combinations(digits):
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return letter_ref[digits[0]]
    previous_combos = letter_combinations(digits[1:])
    new_combos = []
    for combo in previous_combos:
        for letter in letter_ref[digits[0]]:
            new_combos.append(letter + combo)
    return new_combos


print(letter_combinations("23"))
