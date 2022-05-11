# fibonacci series 0,1,1,2,3,5,8,13
final = [0,1]


def x (a, b):
    final.append(a + b)
    return


def y (cycles):
    for num in cycles:
        x(final[-1], final[-2])
    print(final)


y(range(1,11))