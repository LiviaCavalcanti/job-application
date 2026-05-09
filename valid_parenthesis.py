input_string = "({[]})"

def is_valid_parenthesis(s):
    stack = []

    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if char == ")" and top != "(":
                return False
            if char == "}" and top != "{":
                return False
            if char == "]" and top != "[":
                return False
            
    return len(stack) == 0

is_valid = is_valid_parenthesis(input_string)
print(f"Is the input string '{input_string}' valid? {is_valid}")