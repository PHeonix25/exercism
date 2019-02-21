def __validate_input(number):
    if not 1 <= number <= 64:
        raise ValueError("Square number needs to be between 1 and 64")

def on_square(n):
    """
    Given a chess square `n`, we will calculate how many
    grains of wheat stand on that square using the known
    geometric series of exponents: Tn = 2n-1, for given T
    """
    __validate_input(n)
    return 2**(n - 1)

def total_after(n):
    """
    Given a chess square `n`, we will calculate how many
    grains of wheat we have seen from 1..n chess squares
    """
    __validate_input(n)
    return sum(on_square(i) for i in range(1, n+1))