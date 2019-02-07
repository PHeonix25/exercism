def __is_valid(isbn):
    '''Validates the requirements around ISBN's'''
    right_length = len(isbn) == 10
    zonder_check = isbn[:-1]
    check_char = isbn[-1:]

    return right_length \
        and (isbn.isdigit() \
            or (zonder_check.isdigit() \
                and check_char == 'x'))

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
