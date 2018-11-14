class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

class LinkedList:
    def __init__(self, val):
        self.head = Node(val)
    
    def append(self, val):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(val)
        return self.head
    
    def removeIndex(self,index):
        if index == 0:
            res = head.val
            self.head = self.head.next
            return res
        temp = self.head
        for i in range(index-1):
            if temp.next:
                temp = temp.next
            else:
                return -1
        ret = temp.next.val
        temp.next = temp.next.next
        return ret
    
    def removeValue(self, target):
        if self.head.val == target:
            head = head.next
            return target.val
        temp = self.head
        while temp.next:
            if temp.next.val == target:
                temp.next = temp.next.next
                return target
            temp = temp.next
        return -1

    def print(self):
        tempstr = ''
        temp = self.head
        while temp.next:
            tempstr += str(temp.val) + ' ---> '
            temp = temp.next
        tempstr += str(temp.val) + ' ---> None'
        print(tempstr)
         

LL = LinkedList(1)
LL.append(2)
LL.append(3)
LL.append(4)
LL.print()
LL.removeIndex(3)
LL.print()
LL.removeValue(3)
LL.print()