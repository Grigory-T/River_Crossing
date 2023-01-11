# python 3.8.8
# jupyter notebook
# https://en.wikipedia.org/wiki/River_crossing_puzzle

from itertools import combinations
from random import sample
from collections import deque
from time import time


def river_crossing(animals_number, boat_seats_number, hate_number):
    # person start at side 1
    # all animals are on side 1 also
    # person side might contain hates animals (person controls this side)
    # person itself does not occupy seat at boat
    # person can move to other side of river (the only option)
    # choice - how many and which anumals bring to the other side (0 anumals is possible choice)    
    
    side_1 = set(range(animals_number))
    side_2 = set()
    hate_pairs = sample(list(combinations(side_1, 2)), k=hate_number)
    path = f'>>> start                            {side_1 = }, {side_2 = }\n\n'
    
    stack = deque()  # BFS in order to find shortest path
    stack.append((side_1, side_2, path, 1))  
    # store state of both sides, all previouse moves to this point and side-destination
    
    tracer = list()
    tracer.append(tuple([frozenset(side_1),frozenset(side_2),1]))
    # store all state which already have been explored by person. Do not repeat state

    while stack:
        side_1, side_2, path, side = stack.pop()
        
        if not side_1:  # all animals on side 2
            return path, hate_pairs
        
        if side == 1:  # we are on side 1 and we are going to move to side 2
            for cnt in range(0, boat_seats_number + 1):  # we can move no more animals then number of seats
                for tup in combinations(side_1, min(cnt, len(side_1))):  # we can pick anumals differently
                    side_1_ = side_1.copy()
                    side_2_ = side_2.copy()

                    side_1_ -= set(tup)  # change anumal sets
                    side_2_ |= set(tup)  # change anumal sets
                    
                    flag = True
                    for i, j in hate_pairs:
                        if i in side_1_ and j in side_1_:  # check should be after person has moved to side 2
                            flag = False                   # so hate pairs of animals do not allowed in side 1

                    if tuple([frozenset(side_1_), frozenset(side_2_), 2]) in tracer:  # Do not repeat state
                        flag = False

                    if flag:
                        # grow path by one move
                        # update state history
                        # add one element on stack
                        path_ = path + f'move to side 2 {tup!s: >20}       {side_1_ = !s: <30}, {side_2_ = !s: <25}\n'
                        tracer.append(tuple([frozenset(side_1_), frozenset(side_2_), 2]))
                        stack.appendleft((side_1_, side_2_, path_, 2))
        
        if side == 2:  # similar to side 1
            for cnt in range(0, boat_seats_number + 1):
                for tup in combinations(side_2, min(cnt, len(side_2))):
                    side_1_ = side_1.copy()
                    side_2_ = side_2.copy()

                    side_2_ -= set(tup)
                    side_1_ |= set(tup)

                    flag = True
                    for i, j in hate_pairs:
                        if i in side_2_ and j in side_2_:
                            flag = False

                    if tuple([frozenset(side_1_), frozenset(side_2_), 1]) in tracer:
                        flag = False

                    if flag:
                        path_ = path + f'move to side 1 {tup!s: >20}       {side_1_ = !s: <30}, {side_2_ = !s: <25}\n'
                        tracer.append(tuple([frozenset(side_1_), frozenset(side_2_), 1]))
                        stack.appendleft((side_1_, side_2_, path_, 1))

                        
if __name__ == '__main__':
    animals_number = 10
    boat_seats_number = 3  # person himself does not count
    hate_number = 4  # hate pairs generates automatically. Max number is combinations w/o rep of animals_number
    path, hate_pairs = river_crossing(animals_number, boat_seats_number, hate_number)
    print(path)
    print(f'>>> {hate_pairs = }')
