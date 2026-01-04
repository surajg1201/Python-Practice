def fun(x):
    return x*x*x - x*x + 2


def bisection(a, b):

    if (fun(a) * fun(b) >= 0):
        print("You have not assumed right a and b\n")
        return

    c = a
    while ((b-a) >= 0.01):

        c = (a+b)/2

        if (fun(c) == 0.0):
            break

        if (fun(c)*fun(a) < 0):
            b = c
        else:
            a = c

    print("The value of root is : ", "%.4f" % c)


a = -500
b = 600
bisection(a, b)
