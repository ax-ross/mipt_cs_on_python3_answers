def number_trajectories(n):
    K = [1, 1] + [0] * (n - 2)
    for i in range(2, n):
        K[i] = K[i - 1] + K[i - 2]
        if (i + 1) % 3 == 0:
            K[i] += K[i // 3]
    return K[n - 1]
