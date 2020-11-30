def is_power_of_three(number):
    if number == 0:
        return False
    if number % 3 == 0:
        return is_power_of_three(number / 3)
    if number == 1:
        return True
    return False


print(is_power_of_three(1))
print(is_power_of_three(2))
print(is_power_of_three(9))
print(is_power_of_three(900))