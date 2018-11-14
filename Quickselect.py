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

def quickselect(lst, left, right, k):
    s = lomuto(lst, left, right)
    if s == k-1:
        return lst[s]
    elif s > left + k - 1:
        return quickselect(lst, left, s-1, k)
    else:
        return quickselect(lst, s+1, right, k)

print(quickselect([7,6,5,4,3,2,1], 0, 6, 4))
