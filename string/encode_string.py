"""
 Implement both encode("aaabbc") → "3a2b1c" and decode("3a2b1c") → "aaabbc". 
 Then handle edge case: numbers inside the original string.
"""

def encode(s):
    if not s:
        return ""

    encoded = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            ch = s[i - 1]
            if ch.isdigit() or ch == "\\":
                encoded.append(f"{count}\\{ch}")
            else:
                encoded.append(f"{count}{ch}")
            count = 1

    ch = s[-1]
    if ch.isdigit() or ch == "\\":
        encoded.append(f"{count}\\{ch}")
    else:
        encoded.append(f"{count}{ch}")

    return ''.join(encoded)

def decode(encoded):
    if not encoded:
        return ""

    decoded = []
    i = 0

    while i < len(encoded):
        count = 0
        while i < len(encoded) and encoded[i].isdigit():
            count = count * 10 + int(encoded[i])
            i += 1

        if count == 0:
            raise ValueError("Invalid encoding: missing count")

        if i >= len(encoded):
            raise ValueError("Invalid encoding: missing character after count")

        if encoded[i] == "\\":
            i += 1
            if i >= len(encoded):
                raise ValueError("Invalid encoding: dangling escape")

        ch = encoded[i]
        decoded.append(ch * count)
        i += 1
    
    return ''.join(decoded)


print(encode("aaabbc"))      # 3a2b1c
print(decode("3a2b1c"))      # aaabbc

test = "aa56abbc"
encoded_test = encode(test)
print(encoded_test)            # 2a1\51\61a2b1c
print(decode(encoded_test))    # aa56abbc