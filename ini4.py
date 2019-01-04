def sum_odd_int_range(a, b):
    """Sums all odd integers from a through b, inclusively"""
    return sum(i for i in range(a, b + 1) if i % 2 == 1)
