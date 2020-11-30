def rotate_right(triple_tuple):
    return triple_tuple[2], triple_tuple[0], triple_tuple[1]


def rotate_left(triple_tuple):
    return triple_tuple[1], triple_tuple[2], triple_tuple[0]


triple = ('A', 'B', 'C')
print(rotate_left(triple))
print(rotate_right(triple))
