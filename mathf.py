# 제곱근
def sqrt(num):
    x = 0.0
    if num < 0: return 0
    for i in range(-2, 6):
        while x**2 < num:
            x += 10**(-i)
        x -= 10**(-i)
    return round(x, 4)

# 상용로그
def log10(num):
    x = 0.0
    if num < 1: return 0
    for i in range(0, 6):
        while 10**x < num:
            x += 10**(-i)
        x -= 10**(-i)
    return round(x, 4)

# 로그
def log(a, b):
    x = 0.0
    if b <= 0 or a <= 0 or a == 1:
        return 0
    if b >= 1:
        for i in range(0, 6):
            while a**x < b:
                x += 10**(-i)
            x -= 10**(-i)
    elif b < 1:
        for i in range(0, 6):
            while a**x > b:
                x -= 10**(-i)
            x += 10**(-i)
    return round(x, 4)

print(sqrt(4))