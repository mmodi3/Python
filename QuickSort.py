def swap(lst, index1, index2):
    temp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = temp

def lomuto(lst, left, right):
    p = lst[left]
    s = left
    for i in range(left, right):
        if lst[i] < p:
            s += 1
            swap(lst, s, i)
    swap(lst, left, s)
    return s

def quicksort(lst, left, right):
    if right-left > 1:
        s = lomuto(lst, left, right)
        print(str(lst) + " Set: " + str(lst[s]))
        quicksort(lst, left, s)
        quicksort(lst, s+1, right)


def quickSort(lst):
    return quicksort(lst, 0, len(lst))

if __name__ == "__main__":
    lst = []
    while True:
        userinput = input("Give list you would like sorted: ")
        if userinput == 'end':
            break
        lst.append(int(userinput))
    print("Unsorted List: " + str(lst))
    quickSort(lst)
    print ("Sorted List: " + str(lst))