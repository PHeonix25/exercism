def prime_factors(natural_number):
    """
    Uses recursion to calculate all 
    prime factors for a given number.
    """
    if not natural_number > 0:
        raise ValueError("Provided value needs to be greater than 0")

    if natural_number == 1:
        return []

    # Start at 2 to prevent divmod from overflowing
    for i in range(2, natural_number):
        x,y = divmod(natural_number, i) 
        if not y: 
            return [i] + prime_factors(x)

    return [natural_number]