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
    total = 0
    for prime in eratosthenes():
        if prime >= 2000000:
            break
        total += prime

    print total