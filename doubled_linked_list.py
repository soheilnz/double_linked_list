# double linked list be joz jello be qabli nodesham refrence dare
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def creation_Double_LL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "created."

    def Insertion_node(self, nodeValue, location):
        if self.head is None:
            print("the node can not be inserted")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    def Traversal(self):
        if self.head is None:
            print("there is not any node to traverse.")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    def Traverse_Reverse(self):
        if self.head is None:
            print("there is not any node to traverse.")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    def searchValue(self, nodeValue):
        if self.head is None:
            print("there is no element to search.")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    print(tempNode.value)
                tempNode = tempNode.next
            print("there is no element.")

    def DeleteNode(self, location):
        if self.head is None:
            print("there is no list here.")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode
            print("the node has been deleted.")

    def DeleteHole(self):
        if self.head is None:
            print("there is not any node")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("the double linked list has been deleted.")


doubly = DoubleLinkedList()
doubly.creation_Double_LL(5)
doubly.Insertion_node(0, 0)
doubly.Insertion_node(2, 1)
doubly.Insertion_node(1, 0)
doubly.Insertion_node(3, 2)
print([node.value for node in doubly])
# doubly.Traversal()
# doubly.Traverse_Reverse()
# doubly.searchValue(8)
doubly.DeleteNode(0)
print([node.value for node in doubly])
doubly.DeleteNode(1)
print([node.value for node in doubly])
doubly.DeleteNode(2)
print([node.value for node in doubly])
