# 0/1 knapsack
from random import random
import time
#items = [(id, weight, value)]

def build_items(n):
    res = []
    for i in range(n):
        res.append([1+int(600*random()), 1+int(600*random())])
    return res

def powerset(items):
    res = [[]]
    for item in items:
        newset = [r + [item] for r in res]
        res.extend(newset)
    return res

def knapsack_brute_force(items, max_weight):
    knapsack = []
    best_weight = 0
    best_value = 0
    for item_set in powerset(items):
        set_weight = sum(e[0] for e in item_set)
        set_value = sum(e[1] for e in item_set)
        if set_value > best_value and set_weight <= max_weight:
            best_value = set_value
            best_weight = set_weight
            knapsack = item_set
    return [best_value, knapsack]

data = build_items(40)
print(data)
    
# time1 = time.time()
# print(knapsack_brute_force([[383, 282], [436, 598], [413, 139], [276, 566], [100, 49], [432, 495], [251, 103], [170, 593], [359, 537], [436, 400], [64, 205], [18, 390], [223, 144], [145, 476], [224, 390], [267, 6], [381, 376], [44, 27], [477, 231], [486, 533]], 1554))
# time2 = time.time()
# print("TIME: ", time2-time1)