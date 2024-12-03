
def ackermann(m, n):
    """
    Computes the Ackermann function A(m, n) using recursion.
    :param m: Non-negative integer
    :param n: Non-negative integer
    :return: Result of Ackermann function
    """
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))

# Test the function
if __name__ == "__main__":
    m, n = 3, 4  # Example inputs
    print(f"Ackermann({m}, {n}) = {ackermann(m, n)}")

