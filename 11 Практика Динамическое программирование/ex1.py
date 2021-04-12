def number_trajectories(n):
    K = [1, 1, 2] + [0] * (n - 3)
    for i in range(3, n):
        K[i] = K[i - 1] + K[i - 2] + K[i - 3]
    return K[n - 1]
