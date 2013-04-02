num_to_len = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3,
              11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8,
              20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}

def length(n):
    """1 <= n < 1000"""
    a, b, c = n / 100, (n % 100) / 10 * 10, n % 10
    total = 0
    if a:
        total += num_to_len[a] + len('hundred')
        if b or c:
            total += len('and')
    if b == 10:
        total += num_to_len[b+c]
    else :
        if b > 1:
            total += num_to_len[b]
        if c:
            total += num_to_len[c]
    return total

if __name__ == '__main__':
    print sum(map(length, xrange(1, 1001)))