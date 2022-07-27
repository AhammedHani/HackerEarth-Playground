import math

for i in range(int(input())):
    b, g, k = map(int, input().split())
    room = math.ceil(b / k) + math.ceil(g / k)
    print(room)
