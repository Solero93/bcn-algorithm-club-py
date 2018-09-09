"""
/**
 * 10 points
 *
 *
 * Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
 * An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 *
 *
 * You may assume all four edges of the grid are all surrounded by water.
 *
 *
 * Example 1:
 *
 *
 * Input:
 * 11110
 * 11010
 * 11000
 * 00000
 *
 *
 * Output: 1
 * Example 2:
 *
 *
 * Input:
 * 11000
 * 11000
 * 00100
 * 00011
 *
 *
 * Output: 3
 */
"""
from enum import Enum
from typing import List, Union


class Directions(Enum):
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)


def count_islands(map_grid: List[List[Union[int, int]]]) -> int:
    visited = [[False] * len(map_grid[0])] * len(map_grid)
    number_of_islands = 0

    def visit_island(row, column):
        visited[row][column] = True
        for direction in Directions:
            new_row, new_column = row + direction.value[0], column + direction.value[1]

            if not (0 <= new_row < len(visited)) or not (0 <= new_column < len(visited[0])):
                continue

            if map_grid[new_row][new_column] is 1 and not visited[new_row][new_column]:
                visit_island(new_row, new_column)

    for i in range(len(map_grid)):
        for j in range(len(map_grid[i])):
            if map_grid[i][j] is 1 and not visited[i][j]:
                number_of_islands += 1
                visit_island(i, j)

    return number_of_islands
