n = 600851475143
prime_factors = []
for d in xrange(2, int(sqrt(n) + 1)):
    while n % d == 0:
        prime_factors.append(d)
        n /= d
    if n <= 1:
        break

print prime_factors[-1]
