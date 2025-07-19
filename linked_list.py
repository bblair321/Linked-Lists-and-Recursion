class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        Assign the provided 'data' to an instance variable.
        Initialize 'next' to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        Initialize 'head' to None to represent an empty list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        Create a new Node with 'data'.
        Insert it at the front of the list (head).
        Update 'head' to the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        (Optional)
        Create a new Node with 'data'.
        Traverse to the end of the list.
        Set the last node's 'next' reference to the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def _recursive_sum_helper(self, node):
        """
        Helper for recursive_sum.
        Returns 0 if node is None.
        Otherwise returns node.data + recursive call on node.next.
        """
        if node is None:
            return 0
        return node.data + self._recursive_sum_helper(node.next)

    def recursive_sum(self):
        """
        Use recursion to sum all node data in the list.
        """
        return self._recursive_sum_helper(self.head)

    def _recursive_reverse_helper(self, current, prev=None):
        """
        Helper for recursive_reverse.
        Base case: if current is None, return prev (new head).
        Otherwise, swap pointers and recurse.
        """
        if current is None:
            return prev
        next_node = current.next
        current.next = prev
        return self._recursive_reverse_helper(next_node, current)

    def recursive_reverse(self):
        """
        Reverse the list in-place using recursion.
        Updates self.head.
        """
        self.head = self._recursive_reverse_helper(self.head)

    def _recursive_search_helper(self, node, target):
        """
        Helper for recursive_search.
        Returns False if node is None.
        Returns True if node.data == target.
        Otherwise recurse on node.next.
        """
        if node is None:
            return False
        if node.data == target:
            return True
        return self._recursive_search_helper(node.next, target)

    def recursive_search(self, target):
        """
        Return True if target found, else False, using recursion.
        """
        return self._recursive_search_helper(self.head, target)

    def display(self):
        """
        Print the contents of the list for debugging.
        Format output as 'val -> val -> val -> None'
        """
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        elements.append("None")
        print(" -> ".join(elements))
