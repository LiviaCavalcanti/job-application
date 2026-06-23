"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

letters= {1:[], 2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"], 5: ["j", "k","l"], 6:["m", "n", "o"], 7: ["p", "q", "r", "s"], 8:["t", "u", "v"], 9:["w", "x", "y", "z"], 0:[" "]}

def combination(inp: str) -> list[str]:
    out = []
    i = 0
    while i < len(inp):
        if out == []:
            out = letters[int(inp[i])].copy()
            i+=1
        else:
            current_letters= letters[int(inp[i])] 
            temp_out = []
            for elem in out:
                for letter in current_letters:
                    temp_out.append(elem + letter)
            out = temp_out
            i+=1
    return out

print(combination("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"])
print(combination("2") == ["a","b","c"])
print(combination("") == [])
print(combination("579") == ["jpw","jpx","jpy","jpz","jqw","jqx","jqy","jqz","jrw","jrx","jry","jrz","jsw","jsx","jsy","jsz","kpw","kpx","kpy","kpz","kqw","kqx","kqy","kqz","krw","krx","kry","krz","ksw","ksx","ksy","ksz","lpw","lpx","lpy","lpz","lqw","lqx","lqy","lqz","lrw","lrx","lry","lrz","lsw","lsx","lsy","lsz"])