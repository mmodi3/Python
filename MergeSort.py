### START-MERGESORT

def mergeSortRecursive(alist):
   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]
       mergeSortRecursive(lefthalf)
       mergeSortRecursive(righthalf)
       i=0
       j=0
       k=0
       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1
       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1
       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

### END-MERGESORT

if __name__ == "__main__":
    lst = []
    while True:
        userinput = input("Give list you would like sorted: ")
        if userinput == 'end':
            break
        lst.append(int(userinput))
    print("Unsorted List: " + str(lst))
    mergeSortRecursive(lst)
    print ("Sorted List: " + str(lst))
