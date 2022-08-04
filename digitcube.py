for i in range(int(input())):
    a, b = map(int, input().split())
    r, t = b, a

    y = [int(q) for q in str(t)]
    s = sum(y)
    c = s * s * s

    count = 1
    d = 0
    if r == 1:
        print(c)
    else:
        while count != r:
            x = [int(q) for q in str(c)]
            s = sum(x)
            d = s * s * s
            c = d
            count = count + 1
        print(d)