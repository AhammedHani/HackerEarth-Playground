def digsum(n):
    sum = 0
    while (n > 0):
        sum += (n % 10)
        n = n // 10
    return sum


for i in range(int(input())):
    a = int(input())
    while (digsum(a) % 4 != 0):
        a += 1
    print(a)
