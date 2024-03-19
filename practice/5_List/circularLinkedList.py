from listNode import ListNode

class CircularLinkedList:
    def __init(self):
        self.__tail = ListNode("dummy",None)
        self.__tail.next = self.__tail
        self.__numItems = 0 
        

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