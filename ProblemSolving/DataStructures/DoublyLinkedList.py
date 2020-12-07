#HackerRank "Inserting a Node Into a Sorted Doubly Linked List"

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def sortedInsert(head, data):
    """
    Insert a new node into a  sorted doubly linked list given the head and the data to be inserted.
    
    :params: head is the head of the doubly linked list
    :param: data the content to be stored into a new node of the doubly-linked list
    :returns: the head of the new list with the inserted data node
    """
    
    new_node = DoublyLinkedListNode(data)
    
    # Regular inserstion of the list assuming head != null and list elements > 1
    if (head != None and data > head.data):
        position = head
        
        # while loop to find the position that data is to be inserted
        while (data > position.data and position.next != None):
            # at the end of the loop, this is the desired position
            position = position.next
        
        # putting the new node at the end of the list
        if data > position.data and position.next == None:
            position.next = new_node
            new_node.prev = position
        
        # putting the new node in the desired location
        else:
            prev_node = position.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = position
            position.prev = new_node

    # Insert the node at the beginning of the list, if the head is larger than data
    if head.data > data:
        new_node.next = head
        head.prev = new_node
        head = new_node
    
    # If the head is null, then the new_node become the new head
    if head == None:
        head = new_node
        
    return head
