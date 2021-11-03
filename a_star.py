from puzzle import Puzzle
from node import Node


def a_star(start: Puzzle, goal: Puzzle) -> (list[str], int):
    nodes: list[Node] = [Node(start, None, None, 0)]
    explored: list[Puzzle] = []
    count: int = 0
    while nodes:
        nodes.sort(key=lambda x: x.f())
        node = nodes.pop(0)
        explored.append(node.get_puzzle())
        count += 1
        if node.get_puzzle() == goal:
            return node.path_from_start(), count
        else:
            for item in node.expand():
                if item.get_puzzle() not in explored:
                    nodes.append(item)
