"""
/**
 * 5 points
 *
 *
 * Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
 *
 *
 * Note: A leaf is a node with no children.
 *
 * Example:
 *
 * Given the below binary tree and sum = 22,
 *
 * 5
 * / \
 * 4   8
 * /   / \
 * 11  13  4
 * /  \      \
 * 7    2      1
 *
 * return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
 */
"""
from functools import reduce


def has_path_sum_recursive_dfs(list_representation: list, sum_path: int) -> bool:
    remaining = sum_path - list_representation[0]

    if len(list_representation) == 1 and remaining == 0:
        return True
    elif len(list_representation) == 1 or remaining < 0:
        return False

    if has_path_sum_recursive_dfs(list_representation[1], remaining):
        return True
    elif len(list_representation) == 3 and has_path_sum_recursive_dfs(list_representation[2], remaining):
        return True

    return False


def has_path_sum_iterative_bfs(list_representation: list, sum_path: int) -> bool:
    tree = list_representation
    current_level_trees = [tree]

    path_sums = []

    while len(current_level_trees) is not 0:
        for i in range(len(current_level_trees)):
            for j in range(1, len(current_level_trees[i])):
                current_level_trees[i][j][0] += current_level_trees[i][0]

        for sub_tree in current_level_trees:
            is_leaf_node = len(sub_tree) is 1
            if is_leaf_node:
                path_sums.append(sub_tree[0])

        current_level_children = [sub_tree[1:] for sub_tree in current_level_trees if sub_tree[0] <= sum_path]
        current_level_trees = reduce(lambda child1, child2: child1 + child2, current_level_children)

    return sum_path in path_sums
