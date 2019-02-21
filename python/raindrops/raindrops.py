from math import sqrt

def __factors(number):
    """
    Calculates all factors of a number.

    Loosely based off https://stackoverflow.com/a/6800214, 
        but removing the private `list.__add__` method 
        invocation and using `not` instead of `number==0`.
    """
    return set(x for tup in 
        ([i, number//i] for i in 
            range(1, int(sqrt(number))+1) 
            if not number % i) 
        for x in tup)

def raindrops(number):
    """
    Converts a given number into "raindrop-speak". 
    (similar to FizzBuzz: https://en.wikipedia.org/wiki/Fizz_buzz)
    
    We calculate factors of the given number, hold them in a 
    list, then use `in` comparisons to add to our returned value.

    ASSUMES that the list of factors is normally small. 
    """
    result = ''
    factors = list(__factors(number))
    print(f"Given {number}, factors are {factors}.")

    if 3 in factors: result += "Pling"
    if 5 in factors: result += "Plang"
    if 7 in factors: result += "Plong"
    if not result: result = str(number)

    return result
