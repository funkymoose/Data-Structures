# 1. Create Node: 2 datafields - Data, link\reference

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data, end = "--->")
                n = n.ref
            print("Null")
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if n.data==x:
                break
            n = n.ref
        if n is None:
            print("Node is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            self.add_begin(data)
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('Linked list is not empty')

    def delete_begin(self):
        if self.head is None:
            print("Cannot delete node, the Linked List is empty")
        else:
            print(f"Deleted node:{self.head.data}")
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Cannot delete node, the Linked List is empty")

        elif self.head.ref is None:
            print(f"Deleted node:{self.head.data}")
            self.head = None

        else:
            n = self.head
            while n.ref.ref is not None:
                    n = n.ref
            print(f"Deleted node:{n.ref.data}")
            n.ref = None

    def delete_between(self,data):
        if self.head is None:
            print("Cannot delete node, the Linked List is empty")

        elif self.head.data == data:
            self.delete_begin()

        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == data:
                    break
                else:
                    n = n.ref
            if n.ref is None:
                print("Cannot find node")
                return
            print(f"Deleted node:{n.ref.data}")
            n.ref = n.ref.ref


LL1 = LinkedList()
while True:

    i = int(input("Enter the Operation\n1.Create a linked list\n2.Add node at begining\n3.Add node before a node\n4.Add node after a node\n5.Add node at last\n6.Delete begining node \n7.Delete node in between \n8.Delete last node \n9.Display Linked List\n10.Quit\n"))

    if i == 1:
        LL1.insert_empty(input("Enter Node:"))
        LL1.print_LL()
    elif i == 2:
        LL1.add_begin(input("Enter Node:"))
        LL1.print_LL()
    elif i == 3:
        LL1.add_before(input("Enter Node:"), input("Before Node:"))
        LL1.print_LL()
    elif i == 4:
        LL1.add_after(input("Enter Node:"), input("After Node:"))
        LL1.print_LL()
    elif i == 5:
        LL1.add_end(input("Enter Node:"))
        LL1.print_LL()
    elif i == 6:
        LL1.delete_begin()
        LL1.print_LL()
    elif i==7:
        LL1.delete_between(input("Enter Node:"))
        LL1.print_LL()
    elif i == 8:
        LL1.delete_end()
        LL1.print_LL()
    elif i == 9:
        LL1.print_LL()
    elif i == 10:
        break
    else:
        print("Enter a valid input")
    print("===================================================================================")






