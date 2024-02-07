#!/usr/bin/python3
"""Module for singly-linked list data structure"""


class Node:
    """Node class for a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a Node object.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): Reference to the next node in the linked list.
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Get/set the next node of the node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList class representing a sorted singly linked list."""

    def __init__(self):
        """Initialize an empty SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a value into the linked list while maintaining sorted order.

        Args:
            value (int): The value to be inserted.
        """

        node = Node(value)

        if self.__head is None:
            self.__head = node
            return

        if node.data < self.__head.data:
            node.next_node = self.__head
            self.__head = node
            return

        curr = self.__head

        while curr:
            if curr.next_node is None or curr.next_node.data >= node.data >= curr.data:
                node.next_node = curr.next_node
                curr.next_node = node
                return

            curr = curr.next_node

    def __str__(self):
        """Generate a string representation of the linked list."""

        curr = self.__head
        string = ""

        while curr:
            string += str(curr.data) + ("" if curr.next_node is None else "\n")
            curr = curr.next_node

        return string
