def choose(n, k):
    if n < k: return 0
    if k == 0 or n == k: return 1
    def _prod(x, y): return x * y
    return (reduce(_prod, (n - i for i in xrange(k))) /
            reduce(_prod, xrange(1, k+1)))

print choose(40, 20)