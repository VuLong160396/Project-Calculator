def plus(first_number, second_number):
    return first_number+second_number

def minus(first_number, second_number):
    return first_number-second_number

def multi(first_number, second_number):
    return first_number*second_number

def divide(first_number, second_number):
    if second_number == 0:
        raise Exception('Sai cú pháp')
    return first_number/second_number


def calculate(operator, first_number, second_number):
    if operator == "+":
        return plus(first_number, second_number)
    elif operator == "-":
        return minus(first_number, second_number)
    elif operator == "*":
        return multi(first_number, second_number)
    elif operator == "/":
        return divide(first_number, second_number)


