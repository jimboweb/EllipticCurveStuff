from Point import Point
def add_points(p1, p2, A = None):
    if p1.infinity:
        return p2
    if p2.infinity:
        return p1
    x_sum = None
    y_sum = None
    if p1.x == p2.x and p1.y == p2.y:
        rise = p1.y - p2.y
        run = p1.x - p2.x
        m = rise/run
        x_sum = m - p1.x - p2.x
        y_sum = m * (2*p1.x - m**2+p2.x) - p1.y

    else:
        if not A:
            raise ValueError("if p1 and p2 are equal, you must give an argument for A")
        dydx = (3*p1.x**2 + A)
        x_sum = dydx**2/2*p1.y - 2*p1.x
        y_sum = dydx*(3*p1.x-dydx**2)-p1.y
    return Point(x_sum, y_sum)

