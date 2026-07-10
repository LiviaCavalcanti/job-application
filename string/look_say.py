"""
6.8 The look-and-say problem
Write the subsequent number that is derived by describing the previous number ub terns of consecutive digits
"""

def look_say(number):
    # avoid recreating a string everytime adds a new term
    s = []
    digit_count= 1
    i =  1
    while i <= len(number)-1:
        if number[i-1] == number[i]:
            digit_count +=1
        else:
            s += [str(digit_count), number[i-1]]
            digit_count = 1
        i +=1

    s += [str(digit_count), number[i-1]]
    return ''.join(s)


print(look_say('111221'))