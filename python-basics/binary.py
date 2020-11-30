def binary(number):
    result = ''
    if number == 0:
        return '0'
    while number != 0:
        modulo = number % 2
        number = number // 2
        result = str(modulo) + result
    return result