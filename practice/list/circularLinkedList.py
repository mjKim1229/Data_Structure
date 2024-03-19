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
            self.__numItems += 1 
            #마지막 노드 추가시 tail 변경 
            if i == (self.__numItems -1):
                self.__tail = newNode
        else: 
            print("index", i, ": out of bound in insert()")

    def append(self, newItem) -> None:
        dummy = self.__tail.next
        newNode = ListNode(newItem, dummy)
        self.__tail.next = newNode
        self.__tail = newNode
        self.__numItems += 1  
        #print(self.__tail.item)

        
    
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


    # def remove(self, x)
    
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
        #마지막 원소 조회시 
        if x == self.__tail.item:
            return self.__numItems
        
        curr = self.__tail.next.next 
        for index in range(self.__numItems):
            if curr.item == x: 
                return index
            else: 
                curr = curr.next
        return -2  
    
    def isEmpty(self) -> bool:
        return self.__numItems == 0 
    
    def size(self) -> int:
        return self.__numItems
    
    def clear(self):
        self.__tail = ListNode("dummy",None)
        self.__numItems = 0 
    
    def count(self, x) -> int:
        return self.__numItems
    
    def extend(self, a): #a는 iterable
        for i in a: 
            self.append(i) 
    
    # def copy(self) -> b'CircularLinkedList':
    
    # def reverse(self) -> None: 
    
    # def sort(self) -> None:
    #     a = []
    #     for node in self:
    #         a.append(node)
    #     a.sort()
        
    #     self.clear()
    #     for i in a:
    #         self.append(i)

    # def __findNode(self, x) -> (ListNode, ListNode): 
    
    def getNode(self, i: int) -> ListNode:
        if i == self.__numItems:
            return self.__tail
        curr = self.__tail.next
        for index in range(i+1):
            curr = curr.next
        return curr

    
    def printList(self) -> None:
        for node in self:
            print(node)
    
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




