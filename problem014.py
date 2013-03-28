clen_memo = {1: 0}
def collatz_len(n):
    i, m = 0, n
    while True:
        if m in clen_memo:
            clen_memo[n] = i + clen_memo[m]
            break
        else:
            m = m / 2 if m % 2 == 0 else 3 * m + 1
            i += 1

for x in xrange(1, 1000000):
    collatz_len(x)

print max(clen_memo.keys(), key=lambda k: clen_memo[k])