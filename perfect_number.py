def functioon(a):
    b = 0
    for i in range(1, a):
        if a % i == 0:
            b += i
    return b == a


for z in range(1, 1000):
    if functioon(z):
        print("Perfect numbers:", z)

