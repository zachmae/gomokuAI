# implementation of the Monte Carlo method
def monte_carlo_algo(n):
    # n is the number of iterations
    # we want to do
    inside = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            inside += 1
    return 4 * inside / n