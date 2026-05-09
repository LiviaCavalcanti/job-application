"""
You flip a biased coin (P(heads) = 0.6) 10 times. 
What is the probability of getting exactly 7 heads?
"""
# C = n! / (k! * (n-k)!)
#c = 10! / 7! * 3!
c = 10 * 9 *8 / (3*2*1)

prob_one_case = 0.6**7 * 0.4**3
p_7_heads = c * prob_one_case
print(f"The probability of getting exactly 7 heads is: {p_7_heads:.4f}")