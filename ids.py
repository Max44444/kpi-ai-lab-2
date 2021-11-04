from puzzle import Puzzle
from node import Node


def dls(node: Node, goal: Puzzle, depth: int) -> (Node, bool, int):
    if node.depth == depth:
        if node.get_puzzle() == goal:
            return node, True, 1
        else:
            return None, True, 1

    elif depth > node.depth:
        any_flag: bool = False
        count: int = 0
        for child in node.expand():
            found, flag, new_count = dls(child, goal, depth)
            count += 1 + new_count
            if found is not None:
                return found, True, count
            any_flag = flag
        return None, any_flag, count


def ids(start: Puzzle, goal: Puzzle, depth: int = 50) -> (list[str], int):
    for i in range(depth):
        found, flag, count = dls(Node(start, None, None, 0), goal, i)
        if found is not None:
            return found.path_from_start(), count
        elif not flag:
            return None, count
