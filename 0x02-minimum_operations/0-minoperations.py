#!/usr/bin/env python3
"""
    implementation of a greedy algorithm to solve
    a problem
"""
import math


def minOperations(n):
    """finds the minimum operations to print n H's"""
    if n < 2:
        return 0
    operations = 0

    for i in range(2, int(math.sqrt(n) + 1)):
        while n % i == 0:
            operations += i
            n //= i

    if n > 1:
        operations += n

    return operations
