# Sieve of Eratosthenes

def eratosthenes():
    composites = {}
    x = 2
    while True:
        if x not in composites:
            yield x
            composites[x*x] = [x]
        else:
            for prime in composites[x]:
                composites.setdefault(x+prime, []).append(prime)
            del composites[x]
        x += 1


if __name__ == '__main__':
    for i, prime in enumerate(eratosthenes(), start=1):
        if i == 10001:
            print prime
            break
