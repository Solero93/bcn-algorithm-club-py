"""
/**
 * 20 points
 * <p>
 * Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent
 * <p>
 * different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval,
 * CPU could finish one task or just be idle.
 * <p>
 * However, there is a non-negative cooling interval n that means between two same tasks,
 * there must be at least n intervals that CPU are doing different tasks or just be idle.
 * <p>
 * You need to return the least number of intervals the CPU will take to finish all the given tasks.
 * <p>
 * Example 1:
 * Input: tasks = ["A","A","A","B","B","B"], n = 2
 * Output: 8
 * Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 * <p>
 * <p>
 * Note:
 * The number of tasks is in the range [1, 10000].
 * The integer n is in the range [0, 100].
 */
"""
from typing import List


def least_interval(tasks: List[str], n: int) -> int:
    return 0
