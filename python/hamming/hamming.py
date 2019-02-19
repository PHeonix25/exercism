def distance(strand_a=[], strand_b=[]):
    """
    Compares two strands, and returns the count of their differences.

    Raises ValueError if strands are not the same length.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands are not the same length. Cannot compare.")
    
    return sum(1 for (x,y) in zip(strand_a, strand_b) if x != y)