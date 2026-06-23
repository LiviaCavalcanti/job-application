def reverse_words(phrase):
    right_idx = len(phrase)-1
    left_idx = 0

    chars = list(phrase)

    def invert_range(chars, right_idx, left_idx):
        while right_idx > left_idx:
            chars[left_idx], chars[right_idx] = chars[right_idx], chars[left_idx]
            left_idx += 1
            right_idx -= 1
        return chars

    chars = invert_range(chars, right_idx, left_idx)
    begin_range = 0
    idx = 0

    while idx < len(phrase):
        if chars[idx] == ' ':
            chars = invert_range(chars, idx-1, begin_range)
            idx += 1
            begin_range = idx
        else :
            idx += 1
    # invert the last word
    chars = invert_range(chars, idx-1, begin_range)
    return ''.join(chars)

print(reverse_words('ram is costly'))
