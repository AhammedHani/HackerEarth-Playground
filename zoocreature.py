import math

c = 0
d = 0
for i in range(int(input())):
    a, b = map(int, input().split())

    lcm = math.lcm(a, b)
    c=lcm/a
    d=lcm/b
    print(int(c),int(d))