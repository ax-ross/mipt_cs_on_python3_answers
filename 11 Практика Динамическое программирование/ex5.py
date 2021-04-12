def win_pos_queen(n, m):
    field = [[None for j in range(m)] for i in range(n)]

    field[-1][-1] = '-'

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if field[i][j] is None:
                flag = False
                for k in range(j, m):
                    if field[i][k] == '-':
                        flag = True
                for k in range(i, n):
                    if field[k][j] == '-':
                        flag = True

                for k in range(i, n):
                    for z in range(j, m):
                        if k - z == i - j:
                            if field[k][z] == '-':
                                flag = True
                if flag:
                    field[i][j] = '+'
                else:
                    field[i][j] = '-'
    for i in field:
        print(*i)
