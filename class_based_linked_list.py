# Node class represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # The actual data stored in the node
        self.next = None  # A pointer to the next node (initially None)

# LinkedList class manages the chain of nodes
class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    # Insert a new node at the start of the list
    def insert_at_start(self, data):
        new_node = Node(data)     # Create a new node
        new_node.next = self.head # New node points to current head
        self.head = new_node      # Head is updated to the new node

    # Insert a new node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            # If list is empty, new node becomes the head
            self.head = new_node
            return
        current = self.head
        
        # Traverse to the last node
        while current.next:
            current = current.next
        current.next = new_node  # Append new node at the end

    # Insert a new node at a specific index
    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index")
            return
        if index == 0:
            self.insert_at_start(data)
            return
        new_node = Node(data)
        current = self.head
        count = 0
        
        # Traverse to the node just before the desired index
        while current and count < index - 1:
            current = current.next
            count += 1
        if current is None:
            print("Index out of range")
            return
        # Insert the new node by adjusting pointers
        new_node.next = current.next
        current.next = new_node

    # Delete the node at a specific index
    def delete_at_index(self, index):
        if index < 0 or self.head is None:
            print("Invalid index or empty list")
            return
        if index == 0:
            # Delete the head node
            self.head = self.head.next
            return
        current = self.head
        count = 0
        
        # Traverse to the node just before the one to delete
        while current.next and count < index - 1:
            current = current.next
            count += 1
        if current.next is None:
            print("Index out of range")
            return
        # Skip the node at the given index
        current.next = current.next.next

    # Search for a value in the list and return its index
    def search(self, value):
        current = self.head
        index = 0
        # Traverse through the list
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1  # Value not found

    # Display all node values in the list
    def display(self):
        current = self.head
        if current is None:
            print("List is empty")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Marks the end of the list

#testing the code
if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_end(10)
    ll.insert_at_start(5)
    ll.insert_at_end(15)
    ll.insert_at_index(1, 7)

    print("Current List:")
    ll.display()  # Expected: 5 -> 7 -> 10 -> 15 -> None

    index = ll.search(10)
    print("Index of 10:", index)  # Expected: 2

    ll.delete_at_index(1)
    print("After deleting index 1:")
    ll.display()  # Expected: 5 -> 10 -> 15 -> None