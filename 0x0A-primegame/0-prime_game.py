#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """winner determinant function"""
    def sieve(max_n):
        """Precompute prime numbers up to max_n using Sieve of Eratosthenes."""
        primes = [True] * (max_n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime
        for i in range(2, int(max_n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, max_n + 1, i):
                    primes[j] = False
        return primes

    max_n = max(nums)
    primes = sieve(max_n)

    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
