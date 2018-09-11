"""
Given a value V, if we want to make change for V cents, and we have infinite supply of each of C = { C1, C2, .. , Cm}
valued coins, what is the minimum number of coins to make the change?


Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents

Input: coins[] = {9, 6}, V = 11
Output: Minimum 2 coins required
We can use one coin of 6 cents and 1 coin of 5 cents
"""
from typing import List


def minimum_coins(coins: list, change: int) -> int:
    number_of_coins: List[int] = [float('inf')] * (change + 1)
    number_of_coins[0] = 0

    for i in range(1, change + 1):
        for coin in coins:
            if coin <= i:
                leftover = i - coin
                current_solution = 1 + number_of_coins[leftover]
                if current_solution < number_of_coins[i]:
                    number_of_coins[i] = current_solution
    return number_of_coins[change]
