input = [2,3,4,5,13,24,25,30]

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n% 5 ==0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    else:
        return n
    
for num in input:
    print(fizzbuzz(num))