def calculate_min_cost(n, price):
    C = [price[0], price[1] + price[0]] + [None] * (n - 1)
    prev = [0] * (n + 1)
    for i in range(2, n + 1):
        if C[i - 1] < C[i - 2]:
            prev[i] = i - 1
            C[i] = C[i - 1] + price[i]
        else:
            prev[i] = i - 2
            C[i] = C[i - 2] + price[i]
    path = []
    i = n
    while i > 0:
        path.append(i)
        i = prev[i]
    path.append(0)
    return path[::-1]
