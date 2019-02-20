def distance(strand_a=[], strand_b=[]):
    """
    Compares two strands, and returns the count of their differences.
    
    ASSUMES strands are short enough to be evaluated for their length.
    RAISES ValueError if strands are not the same length.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands are not the same length. Cannot compare.")
    
    return sum(x != y for (x,y) in zip(strand_a, strand_b))