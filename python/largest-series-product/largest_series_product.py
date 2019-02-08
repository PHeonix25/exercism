from functools import reduce

def chunked_series(series, length):
    return [series[i:i+length] \
        for i in range(0, len(series), 1) \
        if len(series[i:i+length]) == length]

def largest_product(series=None, size=0):
    # Parameter validation
    if size == 0:
        return 1
    if not series and size > 0:
        raise ValueError("You can't have a span > 0 when series is empty")

    return max([ \
        reduce(lambda acc, inp: acc*inp, \
            [int(c) for c in chunk]) \
                for chunk in chunked_series(series, size)])
