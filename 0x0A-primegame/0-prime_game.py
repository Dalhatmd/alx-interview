#!/usr/bin/python3
""" PrimeGame module """


def isWinner(x, nums):
    def sieve(max_n):
        """Precomputes prime numbers up to max_n """
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False
        return is_prime

    def count_primes(n, is_prime):
        """Counts primes from 1 to n."""
        return sum(is_prime[:n + 1])

    if x < 1 or not nums:
        return None

    max_n = max(nums)
    is_prime = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes(n, is_prime)
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
