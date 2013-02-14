def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print sorted(x_1*x_2 for x_1 in xrange(999, 99, -1)
                     for x_2 in xrange(999, 99, -1)
                     if is_palindrome(str(x_1 * x_2)))[-1]
