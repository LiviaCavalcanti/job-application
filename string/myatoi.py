"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

"""

def myAtoi(s: str) -> int:
    s1 = s.strip()
    out = ""
    sign = ""
    for elem in s1:
        if elem.isdigit():
            out += elem
        else:
            if out != "":
                break
            else:
                if elem.isalpha():
                    break
                if elem == "+" or elem == "-":
                    if sign != "":
                        break
                    sign = elem
                else:
                    # if 
                    break
                    

    if sign == "":
        sign = "+"
    value = int(f"{sign}{out}") if out != "" else 0

    if value < -2**31:
        return -2**31
    if value > 2**31 - 1:
        return 2**31 - 1
    return value

print(myAtoi("- 9123weq8*1-029380219381209381209"))