def pi(n):
    s = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            s += -1 / (2 * i - 1)
        else:
            s += 1 / (2 * i - 1)
    return s


n = int(input())
y = pi(n)
print("{:.8f}".format(y * 4))
