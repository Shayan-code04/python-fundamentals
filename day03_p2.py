def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
for num in range(1, 101):
    if is_prime(num):
        primes.append(num)

print("Primes between 1 and 100:")
print(primes)
print(f"Total primes found: {len(primes)}")