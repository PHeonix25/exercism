def is_armstrong(number):
    total = 0
    number_string = "{}".format(number)
    
    for num in number_string:
        total += int(num) ** len(number_string)

    return total == number
