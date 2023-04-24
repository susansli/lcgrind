class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


def add_two_linked_lists(list1: LinkedList, list2: LinkedList):
    solution_list = LinkedList()
    carry_over = 0

    node1 = list1.head
    node2 = list2.head

    while node1 or node2:
        curr_value = carry_over
        if node1:
            curr_value += node1.data
            node1 = node1.next
        if node2:
            curr_value += node2.data
            node2 = node2.next
        if curr_value >= 10:
            curr_value -= 10
            carry_over = 1
        else:
            carry_over = 0
        if node1 is None and node2 is None and carry_over == 1:
            solution_list.append(curr_value)
            solution_list.append(carry_over)
        else:
            solution_list.append(curr_value)
    return solution_list


first = LinkedList()
first.append(9)
first.append(9)
first.append(9)
first.append(9)
first.append(9)
first.append(9)
first.append(9)

second = LinkedList()
second.append(9)
second.append(9)
second.append(9)
second.append(9)

solution = add_two_linked_lists(first, second)
