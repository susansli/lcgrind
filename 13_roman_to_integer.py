# test cases:
# III = 3
# LVIII = 58
# MCMXCIV = 1994

def convert_roman_numeral(roman_numerals):
    reference = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if len(roman_numerals) == 0:
        return 0

    first_index = 0
    second_index = 1
    integer_value = 0

    while first_index < len(roman_numerals):
        first_value = reference[roman_numerals[first_index]]
        second_value = 0
        if second_index <= len(roman_numerals) - 1:
            second_value = reference[roman_numerals[second_index]]
        if first_value >= second_value:
            integer_value += first_value
            first_index += 1
            second_index += 1
        else:
            integer_value += second_value - first_value
            first_index += 2
            second_index += 2

    return integer_value


print(convert_roman_numeral(''))

