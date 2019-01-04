def slice(s, a, b, c, d):
    """Returns two slices of the string s with a space between.
    Between a and b, and c and d. Both inclusive.
    """
    return f'{s[a:b + 1]} {s[c:d + 1]}'
