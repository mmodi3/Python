from random import random
import time 

def buildItems(val):
    items = []
    for Item in range(val):
        items.append([1 + int(600*random()), 1 + int(600*random())])
    return items

def knapSack(items, maxweight):
    if not items:
        return None
    items.sort(key = lambda x:x[0])
    res = [[[0,[]] for x in range(maxweight + 1)] for x in range(len(items))]
    firstweight = items[0][0]
    firstval = items[0][1]
    for index in range(maxweight + 1):
        if firstweight <= index:
            res[0][index][0] += firstval
            res[0][index][1] += [items[0]]
    for item in range(len(items)):
        itemweight = items[item][0]
        itemvalue = items[item][1]
        for index in range(maxweight + 1):
            if itemweight > index:
                res[item][index] = res[item-1][index]
            else:
                if itemvalue + res[item-1][index-itemweight][0] > res[item-1][index][0]:
                    res[item][index][0] = itemvalue + res[item-1][index-itemweight][0]
                    res[item][index][1] = res[item-1][index-itemweight][1] + [items[item]]
                else:
                    res[item][index] = res[item-1][index]
    return res[-1][-1]

data = buildItems(100)
print(data)
time1 = time.time()
print(knapSack(data, 1554*20))
time2 = time.time()
print("TIME: ", time2-time1)