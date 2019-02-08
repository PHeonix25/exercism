def slices(series="", length=1):

    if not series:
        raise ValueError("Series was an invalid value")
    if length <= 0 or length > len(series):
        raise ValueError("Length was an incorrect value")

    return [series[i:i+length] \
        for i in range(0, len(series), 1) \
        if len(series[i:i+length]) == length]
