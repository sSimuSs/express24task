# Sirojiddin Mustafayev
# 12.01.2022
from typing import Optional


# A single node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next: Node = next


# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    # insertion a single data to the linked list
    def insert(self, data: int):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    # insertion multiple data to the linked list
    def insert_tuple(self, data_list: tuple):
        for data in data_list:
            self.insert(data)

    # print method for the linked list
    def print_ll(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


class Task:
    def __init__(self, ll1: LinkedList, ll2: LinkedList):
        self.ll1 = ll1
        self.ll2 = ll2

    # task processing method
    def do(self) -> LinkedList:
        result_ll = LinkedList()
        result_ll.head = self.addTwoNumbers(self.ll1.head, self.ll2.head)
        return result_ll

    # calculation method
    def addTwoNumbers(self, n1: Optional[Node], n2: Optional[Node], add=0) -> Node:
        val1 = n1.data if n1 else 0
        val2 = n2.data if n2 else 0
        s = val1 + val2 + add
        rtrn = Node(s % 10)
        add = 0
        if s >= 10:
            add = int((s - s % 10) / 10)
        if n1.next or n2.next or add != 0:
            n1next = n1.next if n1.next else Node(0)
            n2next = n2.next if n2.next else Node(0)
            rtrn.next = self.addTwoNumbers(n1next, n2next, add)
        return rtrn


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.insert_tuple((2, 4, 3))  # inserting multiple values to linked list

    ll2 = LinkedList()
    ll2.insert_tuple((5, 6, 4))

    task = Task(ll1, ll2)
    result = task.do()
    print("Result:")
    result.print_ll()
