for a in xrange(1, 1001):
    for b in xrange(a+1, 1001):
        c = 1000 - a - b
        if a + b >= 1000:
            break
        if a*a + b*b == c*c:
            print a*b*c 