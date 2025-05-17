"""Brute-force solution for a simple river crossing puzzle."""

from collections import deque
from itertools import combinations
from random import sample
from typing import Iterable, List, Set, Tuple


State = Tuple[frozenset[int], frozenset[int], int]


def _generate_hate_pairs(animals: Iterable[int], hate_number: int) -> List[Tuple[int, int]]:
    """Return a random list of pairs of animals that cannot be left alone."""

    all_pairs = list(combinations(animals, 2))
    return sample(all_pairs, k=hate_number)


def _has_conflict(side: Set[int], hate_pairs: Iterable[Tuple[int, int]]) -> bool:
    """Return ``True`` if the side contains a forbidden pair."""

    return any(i in side and j in side for i, j in hate_pairs)


def river_crossing(animals_number: int, boat_seats_number: int, hate_number: int):
    """Solve the puzzle and return the path and the hate pairs used."""

    side_1: Set[int] = set(range(animals_number))
    side_2: Set[int] = set()

    hate_pairs = _generate_hate_pairs(side_1, hate_number)

    queue: deque[Tuple[Set[int], Set[int], str, int]] = deque()
    queue.append((side_1, side_2, f">>> start                            {side_1 = }, {side_2 = }\n\n", 1))
    visited: Set[State] = {(frozenset(side_1), frozenset(side_2), 1)}

    while queue:
        side_1, side_2, path, side = queue.popleft()

        if not side_1:
            return path, hate_pairs

        if side == 1:
            current, other, next_side = side_1, side_2, 2
        else:
            current, other, next_side = side_2, side_1, 1

        for cnt in range(boat_seats_number + 1):
            for tup in combinations(current, min(cnt, len(current))):
                current_new = current - set(tup)
                other_new = other | set(tup)

                side_1_new, side_2_new = (
                    (current_new, other_new) if side == 1 else (other_new, current_new)
                )

                if _has_conflict(current_new, hate_pairs):
                    continue

                state = (frozenset(side_1_new), frozenset(side_2_new), next_side)
                if state in visited:
                    continue

                visited.add(state)
                path_new = (
                    path
                    + f"move to side {next_side} {tup!s: >20}       {side_1_new = !s: <30}, {side_2_new = !s: <25}\n"
                )
                queue.append((side_1_new, side_2_new, path_new, next_side))

    # No solution was found
    return None, hate_pairs

                        
if __name__ == '__main__':
    animals_number = 10
    boat_seats_number = 3  # person himself does not count
    hate_number = 4  # hate pairs generates automatically. Max number is combinations w/o rep of animals_number
    path, hate_pairs = river_crossing(animals_number, boat_seats_number, hate_number)
    if path is None:
        print('No solution found.')
    else:
        print(path)
    print(f'>>> {hate_pairs = }')
