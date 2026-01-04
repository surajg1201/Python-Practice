def f(x):
    return x**2 - 2


def secant_method(f, x0, x1, tolerance=1e-7, max_iterations=1000):
    for n in range(max_iterations):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if f_x1 - f_x0 == 0:
            print("Error! Division by zero encountered. No solution found.")
            return None

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(x2 - x1) < tolerance:
            print(f"Root found at: {x2} after {n+1} iterations")
            return x2

        x0, x1 = x1, x2

    print("Exceeded maximum iterations. No solution found.")
    return None


if __name__ == "__main__":
    initial_guess_1 = 1.0
    initial_guess_2 = 2.0
    root = secant_method(f, initial_guess_1, initial_guess_2)
    print(f"Estimated root: {root}")
