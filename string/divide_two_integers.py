"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
"""

# def divide(dividend: int, divisor: int) -> int:
    
#     # default: positive division
#     negative = False
#     if dividend < 0 and divisor < 0:
#         negative = False
#         dividend *= -1
#         divisor *= -1
#     elif dividend < 0 or divisor < 0:
#         negative = True
#         if dividend < 0:
#             dividend *= -1
#         else:
#             divisor *= -1
    
#     quotient = 0
#     rest = 0
#     vals = [1]
#     r = divisor
#     while rest  + r <= dividend:
#         rest += r
#         quotient +=1
#         vals.append(r)
#         if r + r +rest <= dividend:
#             r = r + r
#             vals.append(r)


#     if quotient > 2**31 - 1:
#         return 2**31 - 1
#     if quotient < -2**31:
#         return -2**31
    
#     return quotient if not negative else quotient * (-1)

def divide(dividend: int, divisor: int) -> int:
    
    # default: positive division
    negative = False
    if dividend < 0 and divisor < 0:
        negative = False
        dividend *= -1
        divisor *= -1
    elif dividend < 0 or divisor < 0:
        negative = True
        if dividend < 0:
            dividend *= -1
        else:
            divisor *= -1
    
    quotient = 0
    rest = 0
    vals = [1]
    exp = [0]
    level = 1
    r = divisor
    while r <= dividend:
        vals.append(r)
        if level == 1:
            exp.append(level)
            level +=1
        else:
            exp.append(level)
            level *= 2
        r = r + r       

    i = len(vals) -1
    # print(vals, exp, rest, quotient, dividend)
    while exp[i] != 0 and rest <= dividend:
        
        if vals[i] + rest <= dividend:
            rest += vals[i]
            quotient += exp[i]
            # print(rest, quotient)
        else:
            i -=1 

    result = quotient if not negative else quotient * (-1)

    if result > 2**31 - 1:
        return 2**31 - 1
    if result < -2**31:
        return -2**31
    
    return result
# 715827882
print(divide(dividend=2**31, divisor=3))
print(divide(dividend=1, divisor=1))
print(divide(dividend=-24, divisor=-8))

           
# 8       24      24
# 4    12     12
# 2  6    6  
# 1 3 + 3
