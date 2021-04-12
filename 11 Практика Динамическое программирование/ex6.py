def win_pos_king(n, m):
    field = [[None for j in range(m)] for i in range(n)]

    field[-1][-1] = '-'

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if field[i][j] is None:
                flag = False
                if j == m - 1:
                    if field[i + 1][j] == '-':
                        flag = True
                elif i == n - 1:
                    if field[i][j + 1] == '-':
                        flag = True
                else:
                    if field[i + 1][j] == '-' or field[i][j + 1] == '-' or field[i + 1][j + 1] == '-':
                        flag = True

                if flag:
                    field[i][j] = '+'
                else:
                    field[i][j] = '-'

    for i in field:
        print(*i)
