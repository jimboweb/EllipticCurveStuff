from Point import Point
def add_points(p1, p2, A = None):
    if p1.infinity:
        return p2
    if p2.infinity:
        return p1
    x_sum = None
    y_sum = None
    if p1.x == p2.x and p1.y == p2.y:
        if A is None:
            raise ValueError("if p1 and p2 are equal, you must give an argument for A")
        dydx = (3*p1.x**2 + A)/(2*p1.y)
        print("dydx = ",dydx)
        x_sum = dydx**2 - 2*p1.x
        y_sum = dydx*(3*p1.x-dydx**2)-p1.y
    else:
        rise = p1.y - p2.y
        run = p1.x - p2.x
        m = rise/run
        x_sum = m**2 - p1.x - p2.x
        y_sum = m * (2*p1.x - m**2+p2.x) - p1.y
        # print("rise = ", rise, " run = ", run, " m = ", m)

    return Point(x_sum, y_sum)

A=0
P = Point(2,9)
Q = Point(3,10)
R = Point(-4,-3)
PpQ = add_points(P, Q,A)
print("P + Q = ", PpQ.to_string())
PpQ_pR = add_points(PpQ,R,A)
print("(P + Q) + R) = ", PpQ_pR.to_string())
QpR = add_points(Q,R,A)
print("Q + R = ", QpR.to_string())
P_QpR = add_points(P,QpR,A)
print("P + (Q + R)) = ", P_QpR.to_string())

