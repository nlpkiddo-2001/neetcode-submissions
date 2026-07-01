from typing import List

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val)

        new_node.next = self.head
        self.head = new_node

        if self.size == 0:
            self.tail = new_node
        
        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if self.size == 0:
            self.head = self.tail = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1

            if self.size == 0:
                self.tail = None
            return True
        
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next

        to_delete = prev.next
        prev.next = to_delete.next

        if to_delete == self.tail:
            self.tail = prev
        
        self.size -= 1
        return True



    def getValues(self) -> List[int]:
        values = []
        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        return values
