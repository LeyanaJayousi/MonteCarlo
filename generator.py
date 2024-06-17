def linear_congruential_generator(m, a, c, seed):
    x = seed
    while True:
        yield x
        x = (a * x + c) % m #LCG formula
        
def uniform_random_numbers(seed, a, c, m, n, low, high):
    lcg = linear_congruential_generator(m, a, c, seed)
    generated_numbers = []
    for _ in range(n):
        x = next(lcg)
        normalized = x / m # normalizing to ensure uniform distribution
        new = low + (high - low) * normalized # generating in interval (low, high)
        generated_numbers.append(new)
    return generated_numbers