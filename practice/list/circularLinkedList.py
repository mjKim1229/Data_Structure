from listNode import *

class CircularLinkedList:
    
    def __init__(self):
        self.__tail = ListNode("dummy",None)
        self.__tail.next = self.__tail
        self.__numItems = 0 

    def insert(self, i:int, newItem) -> None:
        if i >=0 and i <= self.__numItems:
            prev = self.getNode(i-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            #마지막 노드 추가시 tail 변경 
            if i == self.__numItems:
                self.__tail = newNode
            self.__numItems += 1 
        else: 
            print("index", i, ": out of bound in insert()")

    def append(self, newItem) -> None:
        newNode = ListNode(newItem, self.__tail.next)
        self.__tail.next = newNode
        self.__tail = newNode
        self.__numItems += 1  

        
    
    def pop(self, *args):
        if len(args) != 0: 
            i = args[0]
        
        if len(args) == 0 or i == -1:
            i = self.__numItems - 1
        
        if (i >= 0 and i <= self.__numItems -1):
            prev = self.getNode(i-1)
            retItem = prev.next.item
            prev.next = prev.next.next
            self.__numItems -= 1 
            if self.__numItems == i:
                self.__tail = prev
            return retItem
        else: 
            return None


    def remove(self, x):
        (prev, curr) = self.findNode(x)
        i = self.index(x)
        #마지막 노드 remove시 
        if i == self.__numItems:
            self.__tail = prev
        if curr != None: #찾아지면 
            prev.next = curr.next 
            self.__numItems -= 1 
            return x 
        else: 
            return None
    
    def get(self, *args):
        if self.isEmpty():
            return None 
        
        if len(args) != 0: 
            i = args[0]
        
        if len(args) == 0 or i == -1:
            i = self.__numItems - 1

        if (i >= 0 and i <= self.__numItems -1):
            return self.getNode(i).item
        else: 
            return None

    def index(self, x) -> int:             
        for index in self:
            if index == x: 
                return count
            count += 1 
        return -2  
    
    def isEmpty(self) -> bool:
        return self.__numItems == 0 
    
    def size(self) -> int:
        return self.__numItems
    
    def clear(self):
        self.__tail = ListNode("dummy",None)
        self.__tail.next = self.__tail
        self.__numItems = 0 
    
    def count(self, x) -> int:
        count = 0 
        for node in self:
            if node == x: 
                count += 1 
        return count
    
    def extend(self, a): #a는 iterable
        for i in a: 
            self.append(i) 
    
    def copy(self) -> b'CircularLinkedList':
        a = CircularLinkedList()
        for i in a: 
            self.append(i)
        return a
    
    def reverse(self) -> None:
        prev = self.__tail
        curr = self.__tail.next
        next_node = curr.next

        while curr != self.__tail:
            curr.next = prev
            prev = curr
            curr = next_node
            next_node = curr.next

        curr.next = prev
        self.__tail = curr
        self.__tail.next = curr.next
        
    
    
    def sort(self) -> None:
        a = []
        for node in self:
            a.append(node)
        a.sort()
        self.clear()
        
        for node in a:
            self.append(node)
    

    def findNode(self, x) -> (ListNode, ListNode):
        prev = self.__tail
        curr = prev.next
        while curr != None:
            if curr.item == x: 
                return (prev, curr)
            else: 
                prev = curr; curr = curr.next
        return (None, None) 
    
    def getNode(self, i: int) -> ListNode:
        if i == self.__numItems:
            return self.__tail
        curr = self.__tail.next
        for index in range(i+1):
            curr = curr.next
        return curr

    
    def printList(self) -> None:
        for node in self:
            print(node,end=" ")
        print()
    
    def __iter__(self): 
        return CircularLinkedlistIterator(self)


class CircularLinkedlistIterator: 
    def __init__(self, alist):
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next 
    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else: 
            item = self.iterPosition.item 
            self.iterPosition = self.iterPosition.next 
            return item 




