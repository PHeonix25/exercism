def __is_valid(isbn):
    '''Validates the requirements around ISBN's'''
    # Check length, this is an easy one...
    if len(isbn) != 10:
        return False

    # It can either be completely numeric, OR numeric + X
    return isbn.isdigit() \
        or (isbn[:-1].isdigit() and isbn[-1:] == 'x')


def __val_to_int(val):
    '''Converts the provided value to an int, with X=10'''
    return int((val, 10)[val == 'x'])


def verify(isbn=''):
    # Tidy up and standardise our input:
    isbn = isbn.replace('-', '').lower()

    if not __is_valid(isbn):
        print(f"Invalid ISBN detected: '{isbn}'.")
        return False

    # Step through each character in the string,
    # converting it to it's equivalent number, and
    # multiplying it by it's distance from the start,
    # then sum all these up to get the total
    total = sum(__val_to_int(val) * (10-idx) \
        for idx, val in enumerate(isbn))

    # If the total is evenly divisible by 11, it is valid
    return total % 11 == 0
