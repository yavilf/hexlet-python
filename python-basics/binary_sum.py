def binary(number):
    result = ''
    if number == 0:
        return '0'
    while number != 0:
        modulo = number % 2
        number = number // 2
        result = str(modulo) + result
    return result


def inverted_string(string):
    inverted = ''
    for i in string:
        inverted = i + inverted
    return inverted


def decimal(string):
    inverted = inverted_string(string)
    decimal_number = 0
    for i, el in enumerate(inverted):
        decimal_number += int(el) * (2 ** i)
    return decimal_number


def binary_sum(first_string, second_string):
    first_number = decimal(first_string)
    second_number = decimal(second_string)
    decimal_sum = first_number + second_number
    return binary(decimal_sum)


print(inverted_string('ABC'))
print(decimal('10110110'))
print(binary_sum('1101', '101'))
print(binary_sum('10', '1'))


