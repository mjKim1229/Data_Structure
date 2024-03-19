from linkedList.listNode import ListNode

class CircularLinkedList:
    
    def __init__(self):
        self.__tail = ListNode("dummy",None)
        self.__tail.next = self.__tail
        self.__numItems = 0 

    # def insert(self, i:int, newItem) -> None: 

    def append(self, newItem) -> None:
        dummy = self.__tail
        newNode = ListNode(newItem, dummy)
        self.__tail.next = newNode
        self.__tail = newNode
        self.__numItems += 1  
    
    # def pop(self, *args):


    # def remove(self, x):
    
    # def get(self, *args):

    # def index(self, x) -> int: 
    
    def isEmpty(self) -> bool:
        return self.__numItems == 0 
    
    def size(self) -> int:
        return self.__numItems
    
    def clear(self):
        self.__tail = ListNode("dummy",None)
        self.__numItems = 0 
    
    # def count(self, x) -> int: 
    
    # def extend(self, a): #a는 iterable 
    
    # def copy(self) -> b'CircularLinkedList':
    
    # def reverse(self) -> None: 
    
    # def sort(self) -> None

    # def __findNode(self, x) -> (ListNode, ListNode): 
    
    def getNode(self, i: int) -> ListNode:
        if i == -1:
            return self.__tail.next
    
    def printList(self) -> None:
        iter = CircularLinkedlistIterator(self)
        print(iter.iterPosition)
    
    # def __iter__(self): 
    #     return CircularLinkedlistIterator(self)


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




