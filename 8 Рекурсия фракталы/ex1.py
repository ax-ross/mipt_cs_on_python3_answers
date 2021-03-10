import sys


def fac(n, depth=0):
    if n <= 1:
        print(f"Depth = {depth}")
        return 1
    depth += 1
    return fac(n - 1, depth) * n


print(fac(996))
print(sys.getrecursionlimit())
