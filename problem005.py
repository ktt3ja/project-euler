def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == '__main__':
    x = 1
    for i in range(2, 21):
        x = (x * i) / gcd(x, i)
    print x