from collections import defaultdict

def tri_nums():
    tri_num = 1
    i = 2
    while True:
        yield tri_num
        tri_num += i
        i += 1

def num_factors(n):
    """
    http://en.wikipedia.org/wiki/Divisor_function
    n = p_1^{a_1} *...* p_k^{a_k}
    return (a_1+1) *...*(a_k+1)
    """
    divisors = defaultdict(int)
    p = 2
    while n > 1:
        while n % p == 0:
            divisors[p] += 1
            n /= p
        if p in divisors:
            divisors[p] += 1
        p += 1

    return reduce(lambda x, y: x * y, divisors.values()) if divisors else 0


if __name__ == '__main__':
    for tri_num in tri_nums():
        if num_factors(tri_num) > 500:
            print tri_num
            break