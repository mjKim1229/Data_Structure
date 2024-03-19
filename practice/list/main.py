from linkedListBasic import LinkedListBasic
from circularLinkedList import CircularLinkedList

if __name__ == "__main__":

    names = ["Amy","Kevin","Mary","David"]

    name_list = LinkedListBasic()
    
    for name in names: 
        name_list.append(name)