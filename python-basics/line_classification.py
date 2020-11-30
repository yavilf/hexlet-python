def is_degenerated(points):
    (x1, y1) = points[0]
    (x2, y2) = points[1]
    return x1 == x2 and y1 == y2


def is_vertical(points):
    (x1, y1) = points[0]
    (x2, y2) = points[1]
    return not(is_degenerated(points)) and x1 == x2


def is_horizontal(points):
    (x1, y1) = points[0]
    (x2, y2) = points[1]
    return not(is_degenerated(points)) and y1 == y2


def is_inclined(points):
    return not(is_degenerated(points) or is_vertical(points) or is_horizontal(points))


line1 = (0, 10), (100, 130)
print(is_vertical(line1))
print(is_horizontal(line1))
print(is_degenerated(line1))
print(is_inclined(line1))