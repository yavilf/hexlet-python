def sort_pair(our_tuple):
    our_first = our_tuple[0]
    our_second = our_tuple[1]
    if our_first < our_second:
        return (our_first, our_second)
    else:
        return (our_second, our_first)


print(sort_pair((7, 9)))