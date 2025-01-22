#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    :param coins: List of coin values available.
    :param total: Total amount to be met.
    :return: Fewest number of coins needed, or -1 if not possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    count = 0

    for coin in coins:
        if total == 0:
            break

        count += total // coin
        total %= coin

    return count if total == 0 else -1
