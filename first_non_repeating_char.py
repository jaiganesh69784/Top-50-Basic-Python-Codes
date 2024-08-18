def first_non_repeating_char(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    for char in s:
        if frequency[char] == 1:
            return char
    return None
