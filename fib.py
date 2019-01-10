def fib(n, k):
    """Returns the total number of rabbits pairs present after n months giving
    birth to k rabbit pairs per generation.
    """
    hej = [1, 1]
    for f in range(2, n):
        hej.append(hej[f - 2] * k + hej[f - 1])
    return hej[-1]


print(fib(32, 4))

# I had forgotten about this approach. I have been using too much C lately.
def fib1(n, k):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, a * k + b
    return b


print(fib1(5, 3))
