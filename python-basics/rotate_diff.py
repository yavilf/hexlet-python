def diff(number1, number2):
    number1 = abs(number1)
    number2 = abs(number2)
    if number1 > number2:
        result = number1 - number2
        rotate_coffee = number1 // 360
        if rotate_coffee > 0:
            result360 = rotate_coffee * 360 - number1 + number2
        else:
            result360 = 360 - number1 + number2
    else:
        result = number2 - number1
        rotate_coffee = number2 // 360
        if rotate_coffee > 0:
            result360 = rotate_coffee * 360 - number2 + number1
        else:
            result360 = 360 - number2 + number1
    if result > result360:
        return result360
    return result


print(diff(0, 0))
print(diff(0, 180))
print(diff(30, 270))
print(diff(0, 720))
print(diff(-720, 0))
