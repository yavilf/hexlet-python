def fizz_buzz(start, stop):
    response = ''
    for i in range(start, stop + 1):
        if i % 3 == 0 and i % 5 == 0:
            response += 'FizzBuzz'
        elif i % 3 == 0:
            response += 'Fizz'
        elif i % 5 == 0:
            response += 'Buzz'
        else:
            response += str(i)
        if i < stop:
            response += ' '
    return response


print(fizz_buzz(7, 7))
print(fizz_buzz(11, 20))
print(fizz_buzz(11, 2))
