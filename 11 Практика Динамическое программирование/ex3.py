def calculate_min_cost(n, price):
    C = [price[0], price[1] + price[0]] + [None] * (n - 1)
    for i in range(2, n + 1):
        C[i] = min(C[i - 1], C[i - 2]) + price[i]
    return C[n]
