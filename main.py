from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """


    ll = LinkedList()

    # 2) Insert some sample data using insert_at_front or insert_at_end
    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    ll.insert_at_front(50)  # List order: 50 -> 20 -> 10 -> 30 -> 40

    # 3) Display the list to verify insertion
    print("Initial list:")
    ll.print_list()

    # 4) Call recursive_sum and print the result
    total = ll.sum()
    print(f"Sum of all nodes: {total}")

    # 5) Call recursive_search with a target and print result
    targets = [30, 99]
    for target in targets:
        found = ll.search(target)
        print(f"Search for {target}: {'Found' if found else 'Not Found'}")

    # 6) Call recursive_reverse, then display the reversed list
    ll.reverse()
    print("Reversed list:")
    ll.print_list()
