# Linked_list
# Linked List Implementation

This project implements a Singly Linked List in Python using object-oriented programming. A Linked List is a linear data structure where each element (called a node) contains:
data: The actual value
next: A reference to the next node in the list

# Components
1. Node Class
Represents an individual element in the linked list.
Attributes:
data: Stores the value of the node
next: Points to the next node (default is None)

2. LinkedList Class
Manages the chain of nodes and provides various operations.
Methods:
insert_at_start(data) → Inserts a node at the beginning
insert_at_end(data) → Adds a node at the end
insert_at_index(index, data) → Inserts a node at a specific index
delete_at_index(index) → Deletes a node at a given index
search(value) → Returns the index of a value, or -1 if not found
display() → Prints all node values in order