s = "3[a]2[a1[bc]]"

def get_subword(string, idx):
    print("in get subword")
    elem = string[idx-1]
    multiplier = ""
    word = ""
    while elem != "]" and idx < len(string):
        print(elem)
        if elem.isdigit():
            multiplier += elem
            print("multiplier")
        elif elem == "[":
            continue
        else:
            word += elem 
        idx += 1
        print(idx)
        elem = string[idx]
        break
    reponse = int(multiplier) * word
    print("reponse", reponse)
    return idx, reponse


def get_word(s, i=0):
    multiplier = ""
    word = ""
    reponse = ""
    while i < len(s):
        print(i)
        elem = s[i]
        print("current elem", elem)
        if elem.isdigit():
            multiplier += elem
        elif elem == "]":
            return i, reponse
        elif elem == "[":
            i, word = get_word(s, i+1)
            reponse += int(multiplier) * word
            multiplier = ""
        else:
            word += elem 
        i += 1
    return reponse

print(get_word(s))