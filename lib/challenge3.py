def highest_value(s):
    vowels = 'aeiou'
    c_value = 0
    mx_value = 0

    for letter in s:
        if letter not in vowels:
            c_value += ord(letter) - ord("a") + 1
        else:
            mx_value = max(mx_value, c_value)
            current_value = 0

    return max(mx_value, c_value)
