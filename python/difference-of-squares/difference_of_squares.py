def square_of_sum(count=1): 
    """Returns the square of the sum of the numbers from 1 to count"""
    return sum(range(1, count+1)) ** 2
    
def sum_of_squares(count=1):
    """Returns the sum of the square of the numbers from 1 to count"""
    return sum(i**2 for i in range(1, count+1))

def difference(count=1):
    """Returns the difference between the square of the sum and \
        the sum of the square of all numbers from 1 to count"""
    return square_of_sum(count) - sum_of_squares(count)
