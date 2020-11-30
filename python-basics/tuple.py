def div_mod(a, b):
    quotient = a // b
    modulo = a % b
    return (quotient, modulo)

tuple_1 = div_mod(13, 4)
print(tuple_1)
(quotient, modulo) = tuple_1
print(tuple_1[0], ' ', modulo)