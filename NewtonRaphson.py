def newton_raphson(f, df, x0, tol=1e-7, max_iter=100):

    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if abs(fx) < tol:
            return x

        if dfx == 0:
            print("Derivative is zero. No solution found.")
            return None

        x = x - fx / dfx

    print("Maximum iterations reached. No solution found.")
    return None


if __name__ == "__main__":
    def f(x):
        return x**2 - 4

    def df(x):
        return 2 * x

    x0 = 3.0

    root = newton_raphson(f, df, x0)

    print(f"Root: {root}")
