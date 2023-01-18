# Given the head of a linked list, remove the nth node from the end of the
# list and return its head *in one pass*

# The "straightforward" way to solve this problem is to get the length of the LL on the 1st pass
# and then do the removal on the 2nd pass. This takes O(2N) time but only O(1) space.

# To do the problem in one pass, I thought about storing some kind of reference to the node that I have
# to backtrack to. By using a dictionary and saving a node each time I iterate from the list I can
# easily tell which node is at the len(head) - n position.

# This solution takes O(N) time and O(N) space.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n):
    node_ref = {}
    temp = head
    counter = 0  # keep track of length

    while temp is not None:
        node_ref[counter] = temp
        temp = temp.next
        counter += 1

    if counter == n:  # means that we're only removing node 1
        head = head.next
        return head

    temp = node_ref[counter - n - 1]  # otherwise set temp to previous node

    if temp.next is not None:  # the removal node exists
        temp.next = temp.next.next
    else:  # the removal node is the end of the list
        temp.next = None
    return head
