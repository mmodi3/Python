import random
import time

def is_sorted(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True

def bogoSortMemoized(data):
    seenDict = {}
    count = 0
    res = []
    while not is_sorted(data):
        count += 1
        print("Unsorted List Fast: " + str(data))
        seenDict[str(data)] = True
        while str(data) in seenDict:
            random.shuffle(data)
    res.append(count)
    res.append(data)
    return res

def bogoSortBruteForce(data):
    res = []
    count = 0
    while not is_sorted(data):
        count += 1
        print("Unsorted List Slow: " + str(data))
        random.shuffle(data)
    res.append(count)
    res.append(data)
    return res

if __name__ == "__main__":
    lst1 = []
    lst2 = []
    while True:
        userinput = input("Give list you would like sorted: ")
        if userinput == 'end':
            break
        lst1.append(int(userinput))
        lst2.append(int(userinput))
    print("Unsorted List: " + str(lst1))
    lst1 = bogoSortMemoized(lst1)
    print("FAST BOGOSORT: " + "Sorted List: " + str(lst1[1]) + " Number of Steps: " + str(lst1[0]))
    time.sleep(10)
    lst2 =  bogoSortBruteForce(lst2)
    print("Slow BOGOSORT: " + "Sorted List: " + str(lst2[1]) + " Number of Steps: " + str(lst2[0]))
