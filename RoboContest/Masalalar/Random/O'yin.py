def solve(n):
    # Eratosfen g'alviri bilan tub sonlar sonini topamiz
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    prime_count = sum(sieve)
    return "Ali" if prime_count % 2 == 1 else "Bobur"


n = int(input())
print(solve(n))