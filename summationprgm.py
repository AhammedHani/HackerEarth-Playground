import math


def sum(n):
    root = (int)(math.sqrt(n))
    ans = 0

    for i in range(1, root + 1):
        ans = ans + n // i

    ans = 2 * ans - (root * root)
    return ans


for _ in range(int(input())):
    n = int(input())
    print((sum(n)))
