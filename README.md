# River_Crossing
River crossing puzzle

Example of one round:

In:
animals_number = 10
boat_seats_number = 3  # person himself does not count
hate_number = 4  # hate pairs generates automatically. Max number is combinations w/o rep of animals_number

Out:
>>> start                            side_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, side_2 = set()

move to side 2               (1, 5)       side_1_ = {0, 2, 3, 4, 6, 7, 8, 9}      , side_2_ = {1, 5}                   
move to side 1                 (1,)       side_1_ = {0, 1, 2, 3, 4, 6, 7, 8, 9}   , side_2_ = {5}                      
move to side 2            (0, 2, 8)       side_1_ = {1, 3, 4, 6, 7, 9}            , side_2_ = {0, 8, 2, 5}             
move to side 1                   ()       side_1_ = {1, 3, 4, 6, 7, 9}            , side_2_ = {0, 8, 2, 5}             
move to side 2            (3, 4, 6)       side_1_ = {1, 7, 9}                     , side_2_ = {0, 2, 3, 4, 5, 6, 8}    
move to side 1                   ()       side_1_ = {1, 9, 7}                     , side_2_ = {0, 2, 3, 4, 5, 6, 8}    
move to side 2            (1, 9, 7)       side_1_ = set()                         , side_2_ = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

>>> hate_pairs = [(1, 8), (5, 7), (1, 5), (5, 9)]
